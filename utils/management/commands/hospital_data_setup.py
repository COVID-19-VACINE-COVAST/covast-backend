import requests
import xmltodict

from django.conf import settings


COVID19_HOSPITAL_BASE_API_URL = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList?ServiceKey={' \
                                'service_key}&pageNo={page_no}&numOfRows={num_of_rows}&spclAdmTyCd={type_code}'
COVID19_HOSPITAL_SERVICE_KEY = settings.COVID19_HOSPITAL_SERVICE_KEY

COVID19_HOSPITAL_NUM_OF_ROWS = 10  # 한 페이지 결과 수
COVID19_HOSPITAL_PAGE_NO = 1  # 페이지 번호
COVID19_HOSPITAL_TYPE_CODE_LIST = ['A0', '97', '99']  # A0: 국민안심병원, 97: 코로나검사실시기관, 99: 코로나 선별진료소 운영기관

KAKAO_REST_API_KEY = settings.KAKAO_REST_API_KEY
KAKAO_API_BASE_URL = 'https://dapi.kakao.com/v2/local/search/keyword.json?&query={address}'


def get_hospital_data():
    request_url = COVID19_HOSPITAL_BASE_API_URL .format(service_key=COVID19_HOSPITAL_SERVICE_KEY, page_no=COVID19_HOSPITAL_PAGE_NO,
                                                        num_of_rows=COVID19_HOSPITAL_NUM_OF_ROWS, type_code=COVID19_HOSPITAL_TYPE_CODE_LIST[2])

    xml_result = requests.get(request_url)
    json_result = xmltodict.parse(xml_result.content)
    hospital_list = json_result['response']['body']['items']['item']

    for hospital in hospital_list:
        print(hospital)
        address = f"{hospital['sidoNm']} {hospital['sgguNm']} {hospital['yadmNm']}"
        get_hospital_geo_data(address)

def get_hospital_geo_data(address):
    request_url = KAKAO_API_BASE_URL .format(address=address, rest_api_key=KAKAO_REST_API_KEY)
    print(address)

    json_result = requests.get(request_url, headers={
        'Authorization': f'KakaoAK {KAKAO_REST_API_KEY}'
    }).json()
    print(json_result)
    # Todo: 카카오 API 에서 명칭으로 검색 시 결과가 하나도 나오지 않는 경우가 있음. ex) 서울 감동구 성심의료재단강동성심병원
    if not json_result['meta']['total_count'] == 0:
        print(json_result['documents'][0])


get_hospital_data()
