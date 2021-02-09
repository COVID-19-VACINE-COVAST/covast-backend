import requests
import xmltodict

from django.core.management.base import BaseCommand
from django.conf import settings

from inoculation.models.hospital import Hospital


class Command(BaseCommand):
    def __init__(self):
        self.COVID19_HOSPITAL_BASE_API_URL = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList?ServiceKey={' \
                                             'service_key}&pageNo={page_no}&numOfRows={num_of_rows}&spclAdmTyCd={type_code}'
        self.COVID19_HOSPITAL_SERVICE_KEY = settings.COVID19_HOSPITAL_SERVICE_KEY

        self.COVID19_HOSPITAL_NUM_OF_ROWS = 10  # 한 페이지 결과 수
        self.COVID19_HOSPITAL_PAGE_NO = 1  # 페이지 번호
        self.COVID19_HOSPITAL_TYPE_CODE_LIST = ['A0', '97', '99']  # A0: 국민안심병원, 97: 코로나검사실시기관, 99: 코로나 선별진료소 운영기관

        self.KAKAO_REST_API_KEY = settings.KAKAO_REST_API_KEY
        self.KAKAO_API_BASE_URL = 'https://dapi.kakao.com/v2/local/search/keyword.json?&query={address}'

        super().__init__()

    def get_hospital_data(self):
        request_url = self.COVID19_HOSPITAL_BASE_API_URL.format(service_key=self.COVID19_HOSPITAL_SERVICE_KEY,
                                                                page_no=self.COVID19_HOSPITAL_PAGE_NO,
                                                                num_of_rows=self.COVID19_HOSPITAL_NUM_OF_ROWS,
                                                                type_code=self.COVID19_HOSPITAL_TYPE_CODE_LIST[2])

        xml_result = requests.get(request_url)
        json_result = xmltodict.parse(xml_result.content)
        hospital_list = json_result['response']['body']['items']['item']

        hospital_objs_data_list = []
        for hospital in hospital_list:
            address = f"{hospital['sidoNm']} {hospital['sgguNm']} {hospital['yadmNm']}"
            hospital_data = self.get_hospital_geo_data(address)

            if hospital_data:
                try:
                    Hospital.objects.get(latitude=hospital_data['latitude'], longitude=hospital_data['longitude'])

                    print(f'Result is already exists: {address}')
                except Hospital.DoesNotExist:
                    hospital_objs_data_list.append(Hospital(
                        name=hospital_data['name'],
                        address=hospital_data['address'],
                        road_address=hospital_data['road_address'],
                        contact=hospital_data['contact'],
                        place_url=hospital_data['place_url'],
                        latitude=hospital_data['latitude'],
                        longitude=hospital_data['longitude'],
                    ))
                except Exception as e:
                    print(e)
            else:
                print(f'Result not found: {address}')

        Hospital.objects.bulk_create(hospital_objs_data_list)

    def get_hospital_geo_data(self, address):
        request_url = self.KAKAO_API_BASE_URL.format(address=address, rest_api_key=self.KAKAO_REST_API_KEY)

        json_result = requests.get(request_url, headers={
            'Authorization': f'KakaoAK {self.KAKAO_REST_API_KEY}'
        }).json()
        # Todo: 카카오 API 에서 명칭으로 검색 시 결과가 하나도 나오지 않는 경우가 있음. ex) 서울 감동구 성심의료재단강동성심병원

        data_key_list = ['place_name', 'address_name', 'road_address_name', 'phone', 'place_url', 'x', 'y']
        if not json_result['meta']['total_count'] == 0:
            result = json_result['documents'][0]

            name, address, road_address, contact, place_url, latitude, longitude = [result[data_key] for data_key in data_key_list]

            return {
                'name': name,
                'address': address if address else result['address'],  # 주소 값이 address_name 또는 address 에 담길 경우가 있음
                'road_address': road_address,
                'contact': contact,
                'place_url': place_url,
                'latitude': latitude,
                'longitude': longitude,
            }

    def handle(self, *args, **options):
        self.get_hospital_data()
