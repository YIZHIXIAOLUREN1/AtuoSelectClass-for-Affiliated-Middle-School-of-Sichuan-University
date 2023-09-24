import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor

cookies = {
}#自行获取

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'schoolName=%u56DB%u5DDD%u7701%u6210%u90FD%u5E02%u7B2C%u5341%u4E8C%u4E2D%u5B66%u9AD8%u4E2D%u90E8; schoolLogo=um/pictureNoLogin/510100010038LOGO/510100010038/510100010038_20220617143024433.jpg; userActualName=%u5E78%u5CFB%u6BC5; userLoginName=51068120070223001X; userType=4; userId=3377756; JSESSIONID=7F347533C81D6D8159474B5BA3F1FC7E; sid=ae2b4087-bc4d-4dcf-992d-e82a7561c6b4; accessKeyId=STS.NUosdxDxnxyPJLF7KcjusJc6M; accessKeySecret=FM8sDSFRWLoAFEtLsPdy5njsBWwMyGdR9NQG1dxj2HeH; stsToken=CAIS/gF1q6Ft5B2yfSjIr5baON7MqadPz7u7SGr300s2Zvpfpaadrzz2IHhMe3FpCOkWtPk+mWFZ6f0ZlqB6T55OSAmcNZIoFGjTH8f4MeT7oMWQweEuuv/MQBquaXPS2MvVfJ+OLrf0ceusbFbpjzJ6xaCAGxypQ12iN+/m6/Ngdc9FHHP7D1x8CcxROxFppeIDKHLVLozNCBPxhXfKB0ca3WgZgGhku6Ok2Z/euFiMzn+Ck7JF99Wof8H+NpY3bcogC+3YhrImKvDztwdL8AVP+atMi6hJxCzKpNn1ASMKu03Za7OFq401cV4kN/llQPVewv/njuZkofwJUU8UYd3MVxqAAVAawCGa1hp7ejAyIn7H9RTlkUphSW3BzUqY0qe8Q8l0HNQ+2cb2wBRcg5PN/WePxwG87wc+S8bQEMIw0h8jWIX3ouSeHInqpmtsjANNE/zuX/0ku7znYfurAVIy1ehfow6nbs6PyNEbckGMW2k81mJu4eD6Cr7+oan1aDiR5IYrIAA=',
    'Origin': 'https://whqjyy-school.wuhousmartedu.com',
    'Referer': 'https://whqjyy-school.wuhousmartedu.com/main.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36',
    'request_token': 'null',
    'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def task(openCourseInfoId,openCourseSetId,courseId,kid):

    json_data = {
        'openCourseInfoId': openCourseInfoId,#1
        'openCourseSetId': openCourseSetId,#2
        'courseId': courseId,#1
    }#1在课程界面刷新抓包getCourseinfoDetail,2在课程列表抓包selectCourseList

    while True:
        response = requests.post(
            'https://whqjyy-school.wuhousmartedu.com/student/studentApply',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        print(response.text," ",kid)
        res = json.loads(response.text)
        localtime=time.asctime(time.localtime(time.time()))
        if res["code"] == -1:
            print(localtime,"失败",kid)
            time.sleep(1)
            continue
        flag = res['code']
        if flag == '-1':
            print(localtime,"人满",kid)
        if flag == '0':
            print(localtime,res["msg"],kid)
        if flag == '1':
            print(localtime,"成功",kid)
            break

        time.sleep(1)

def run():
    ke = [[6253,775,7597,1],#请自行更新数据，对应json_data
          [6277,776,7621,2],#最后一位用来输出是哪个课程
          ]
    with ThreadPoolExecutor(2) as t:
        for k in ke:
            openCourseInfoId=k[0]
            openCourseSetId=k[1]
            courseId=k[2]
            kid=k[3]
            t.submit(task,openCourseInfoId,openCourseSetId,courseId,kid)

if __name__ == '__main__':
    run()
