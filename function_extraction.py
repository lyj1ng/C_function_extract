import os
import re

def get_functions(filename):
    rgl_exp1 = r'(.*)(\s)*((void)|(char)|(short)|(int)|(float)|(long)|(double)|(ulong))(\s)(.*)'
    #use to match function name
    pat1 = re.compile(rgl_exp1,re.X)
    with open(filename) as fp:
        front=0
        buffer=[]
        all_func=[]
        func=''
        comment=0
        while True:
            line = fp.readline()
            #if comment : pass
            if '/*' in line[:2]:
                comment+=line.count('/*')
                comment-=line.count('*/')
            elif '*/' in line:
                comment-=line.count('*/')
            elif comment==1 or line[:2]=='//':
                continue
            elif line:
                if '{' in line:
                    if front==0:
                        #if it's the first '{' : find this function's name from its buffer
                        for ind,content in enumerate(buffer):
                            if (pat1.match(content) and ';' not in content) or 'main(' in content:
                                func += ''.join(buffer[ind:])   #add the content before '{' to FUNC
                                buffer=[]                       #clear the buffer
                                break
                    func+=line                                  #add this line to FUNC
                    front+=line.count('{')                      #record the '{'  -  '}' number
                elif '}' in line:
                    func+=line
                    front-=line.count('}')
                    if front==0:
                        all_func.append(func)                # if it's end of the function : add FUNC to ALL_FUNCS
                        func=''                              # clear FUNC
                else:
                    if front==0:                             #if it's regular content:if in the{ }:add to FUNC
                        buffer.append(line)                                                 #else : add to BUFFER                     
                    elif front>0:
                        func+=line
            else:#if line==None:end of file
                break
    return all_func
    
#test code:
for i in get_functions('sal_module_wrapper.c'):
    print(i)
    print('='*90)
    
# demo：
'''
int tos_sal_module_register(sal_module_t *module)
{
    if (!g_sal_module) {
        g_sal_module = module;
        return 0;
    }

    return -1;
}

==========================================================================================
int tos_sal_module_register_default()
{
    g_sal_module = NULL;

    return 0;
}

==========================================================================================
int tos_sal_module_init(void)
{
    if (g_sal_module && g_sal_module->init) {
        return g_sal_module->init();
    }
    return -1;
}

==========================================================================================
int tos_sal_module_parse_domain(const char *host_name, char *host_ip, size_t host_ip_len)
{
    if (g_sal_module && g_sal_module->parse_domain) {
        return g_sal_module->parse_domain(host_name, host_ip, host_ip_len);
    }
    return -1;
}

==========================================================================================
int tos_sal_module_connect(const char *ip, const char *port, sal_proto_t proto)
{
    if (g_sal_module && g_sal_module->connect) {
        return g_sal_module->connect(ip, port, proto);
    }
    return -1;
}

==========================================================================================
int tos_sal_module_send(int sock, const void *buf, size_t len)
{
    if (g_sal_module && g_sal_module->send) {
        return g_sal_module->send(sock, buf, len);
    }
    return -1;
}

==========================================================================================
int tos_sal_module_recv(int sock, void *buf, size_t len)
{
    if (g_sal_module && g_sal_module->recv) {
        return g_sal_module->recv(sock, buf, len);
    }
    return -1;
}

==========================================================================================
int tos_sal_module_recv_timeout(int sock, void *buf, size_t len, uint32_t timeout)
{
    if (g_sal_module && g_sal_module->recv_timeout) {
        return g_sal_module->recv_timeout(sock, buf, len, timeout);
    }
    return -1;
}

==========================================================================================
int tos_sal_module_sendto(int sock, char *ip, char *port, const void *buf, size_t len)
{
    if (g_sal_module && g_sal_module->sendto) {
        return g_sal_module->sendto(sock, ip, port, buf, len);
    }
    return -1;
}

==========================================================================================
int tos_sal_module_recvfrom(int sock, void *buf, size_t len)
{
    if (g_sal_module && g_sal_module->recvfrom) {
        return g_sal_module->recvfrom(sock, buf, len);
    }
    return -1;
}

==========================================================================================
int tos_sal_module_recvfrom_timeout(int sock, void *buf, size_t len, uint32_t timeout)
{
    if (g_sal_module && g_sal_module->recvfrom_timeout) {
        return g_sal_module->recvfrom_timeout(sock, buf, len, timeout);
    }
    return -1;
}

==========================================================================================
int tos_sal_module_close(int sock)
{
    if (g_sal_module && g_sal_module->close) {
        return g_sal_module->close(sock);
    }
    return -1;
}

==========================================================================================
'''
