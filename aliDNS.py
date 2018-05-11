import socket
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest, DescribeDomainRecordsRequest, \
    DescribeDomainRecordInfoRequest, AddDomainRecordRequest
from aliyunsdkcore import client
import json


# 记录本机IP
ip = socket.gethostbyname(socket.gethostname())
print(ip)


# 主域名 如：baidu.com
dns_domain = ''

# Access Key ID
access_key_id = ''

# Access Key Secret
access_Key_secret = ''

# DNS 或者一级域名二级域名前缀  譬如 3q.baidu.com  这里填入3q
DNS_RR = ''
# 记录类型:A或者CNAME,默认为A
dns_type = 'A'
# 记录值：需要修改的ip
dns_value = ip
# dnsID,每一个主机记录都会有一个ID

# 获取dns记录信息列表
def check_records(dns_domain=dns_domain):
    clt = client.AcsClient(access_key_id, access_Key_secret, 'cn-hangzhou')
    request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    request.set_DomainName(dns_domain)
    request.set_accept_format('json')
    result = clt.do_action(request)
    res = result.decode('gb2312')
    result1 = json.JSONDecoder().decode(res)
    list = result1['DomainRecords']['Record']
    print(list)
    return list

# 查询 dns_record_id
def select_RR(list):
    for i in  list:
        print(i)
        if i['RR'] == DNS_RR:
            dns_record_id = i['RecordId']
            print(dns_record_id)
    return dns_record_id

#  更新记录
def update_dns(dns_rr='ip', dns_type='A', dns_value=dns_value, dns_record_id='', dns_ttl='600', dns_format='json'):
    clt = client.AcsClient(access_key_id, access_Key_secret, 'cn-hangzhou')
    request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    request.set_RR(dns_rr)
    request.set_Type(dns_type)
    request.set_Value(dns_value)
    request.set_RecordId(dns_record_id)
    request.set_TTL(dns_ttl)
    request.set_accept_format(dns_format)
    result = clt.do_action(request)
    print(result)
    return result

if __name__ == '__main__':
    list = check_records()
    dns_record_id = select_RR(list)
    update_dns(dns_record_id=dns_record_id)