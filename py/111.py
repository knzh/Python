import requests
from lxml import etree

class TieBa(object):
    def __init__(self,query_string):
        self.query_string = query_string
        self.url = "https://tieba.baidu.com/f"      #目标
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    def params(self):
        para = {
            'kw':self.query_string
        }
        return para

    #1.发送请求
    def send_request(self,url,parms={}):
        response = requests.get(url,params=parms,headers=self.headers)
        return response.content



    #2.数据清洗
    def parse_data(self,data,rule):
        html_data = etree.HTML(data)
        data_list = html_data.xpath(rule)
        print(data_list)





    #3.保存数据
    def save_data(self):
        pass

    #主要的运行逻辑
    def run(self):
        tieba_parames = self.params()
        datas = self.send_request(self.url,tieba_parames)

        #xpath解析
        detail_rule ='//div[@class="t_con clesfix"]/div/div/div/a/text()'
        self.parse_data(datas,detail_rule)



if __name__ == "__main__":
    a = input("请输入你要查询的关键字： ")
    tieba=TieBa(a)
    tieba.run()