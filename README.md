# aliyun_ip_DDNS
基于阿里云SDK

## 使用范围
github上大多数以python2.7为主，此程序为python3。

阿里云的DDNS动态域名解析

将本机或者指定机器的动态ip到域名解析

## 依赖

socket

json

阿里云SDK

pip install aliyun-python-sdk-core-v3



## 参数说明


主域名 如：baidu.com
dns_domain = ''

阿里云的Access Key ID
access_key_id = ''

阿里云的Access Key Secret
access_Key_secret = ''

DNS 或者一级域名二级域名前缀  譬如 3q.baidu.com  这里填入3q
DNS_RR = ''

记录类型:A或者CNAME,默认为A
dns_type = 'A'

记录值：需要修改的ip
dns_value = ip


## 函数说明


### 获取dns记录信息列表

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

用于获取DNS记录列表

### 查询 dns_record_id
	
	def select_RR(list):
	    for i in  list:
	        print(i)
	        if i['RR'] == DNS_RR:
	            dns_record_id = i['RecordId']
	            print(dns_record_id)
	    return dns_record_id

通过list查询获得RecordId。


### 更新(修改)ip记录

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


## 使用说明

程序可设定定时启用或开机启用，使用者应保证依赖正确并且是pyhton3以上。

程序可直接定时运行，使用者填写参数并保证正确。

当指定自己的RecordId，可之调用update_dns方法。


