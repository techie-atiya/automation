from re import search
var_date=""
var_user=""
var_password=""
var_ip=""
date='date'
get_rpc='''<get xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <filter>
      <syslog xmlns="http://netconf/IP">
        <log-actions>
          <remote>
            <destination>
              <name>atiya</name>
            </destination>
          </remote>
        </log-actions>
      </syslog>
    </filter>
  </get>'''
response='''<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply xmlns="xml:ns:netconf:base:1.0" message-id="123455" xmlns:nc="ns:netconf:base:1.0"><data><syslog xmlns="http://netconf/netconf/syslog"><log-actions><remote><destination><name>atiya</name><udp><address>192.168.17.129</address><port>122</port></udp><log-selector><log-facility><facility>all</facility><severity>info</severity><severity-operator>not-</severity-operator></log-facility></log-selector></destination></remote></log-actions></syslog></data></rpc-reply>'''
def snmp_set(data, oid):
	global var_date
	global var_user
        global var_password
        global var_ip
        status= "suceessful"
        
	#snmpset -v2c community string {oid 1.1.1.1.} {value atiya} -format{oid,data}
	if oid == '0.1.0.1.2.3':
        	var_date=data
		#print("res",var_date)
		return(status)
                

	if oid == '0.1.0.1.2.4.1' :
		var_user=data
	else:
		print("no oid matched to set value")
        if oid =='0.1.0.1.2.4.2':
                var_password=data
                
        if oid =='0.1.0.1.2.5.3':
                var_ip=data
        
        


def snmp_get(oid):
	#value=snmpget -v2c community string {oid 1.1.1.1.} -format{oid}
	if oid == '0.1.0.1.2.3' :
		return var_date
	if oid =='0.1.0.1.2.4.1':
		return var_user
        if oid =='0.1.0.1.2.4.2':
                 return var_password
        if oid =='0.1.0.1.2.5.3':
                return var_ip
        
def cli_get(command):
	if command == 'show clock' :
		#print("hi",var_date)
		return var_date
	if command =='show user':
		return var_user
        if command =='show password':
                return var_password
        if command =='show ip':
               return var_ip
def netconf_get(get_rpc):
	if search('IP', str(get_rpc)):
       		 if search('atiya', str(get_rpc)):
           		return response
        else:
           print(" Status:  not found")
           return True
	

def automation():
	print("hi")
	oid='0.1.0.1.2.3'
	data="22 May 2021"
        var=snmp_set(data,oid)
        print("status value:",var)
        
	get_snmp_value=snmp_get(oid)
	print("snmp value",get_snmp_value)
 
        command='show clock'
	get_cli_value=cli_get(command)
	print("cli value",get_cli_value)
	if search(get_cli_value,str(get_snmp_value)):
		print("Test Case pass")
	else :
		print("testcase fail")
	
	oid='0.1.0.1.2.4.1'
	data="atiya"
	snmp_set(data,oid)
	get_snmp_user_value=snmp_get(oid)
	print("snmp get value",get_snmp_user_value)
	command='show user'
	get_cli_value=cli_get(command)
	print("cli get value",get_cli_value)

	if search(str(get_cli_value),str(get_snmp_user_value)):
		print("User Test case pass")
	else:
		print("User Test case fail")
       	oid='0.1.0.1.2.4.2'
        data="password"
        get_snmp_var_password=snmp_get(oid)
        print("snmp get value",get_snmp_var_password)
        command='show password'
        get_cli_value=cli_get(command)
        print("cli get value",get_cli_value)
        if search(str(get_cli_value),str(get_snmp_var_password)):
                 print("Password Test case pass")
        else:
                 print("Password Test case fail")

        

        oid='0.1.0.1.2.5.3'
        data="ip"
        snmp_set(data,oid)
        get_snmp_var_ip=snmp_get(oid)
        print("snmp get value",get_snmp_var_ip)
        command='show ip'
        get_cli_value=cli_get(command)
        print("cli get value",get_cli_value)
        if search(str(get_cli_value),str(get_snmp_var_ip)):
                print("ip test case pass")
        else:
               print("ip test case fail")
        #print(get_rpc)
        rpc_response=netconf_get(get_rpc)
        #print("rpc get value",rpc_response)
        if search(str("192.168.17.129"),str(rpc_response)):
                 print("ip adress is true")
                 print("test case pass")
        else:
                 print("test case fail")
                 
         
      
        

if __name__ == '__main__':
	automation()

