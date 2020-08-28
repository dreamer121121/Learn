# string  = "aa abd edaf 123"
# target = "ded"
# str_list = string.split()
# s = "".join(str_list) #没有空格的字符串
# print(str_list)
#
# index = s.find(target)
#
# cnt = 0
# i = 0
# while cnt <= index:
#     if string[i] != " ":
#         cnt += 1
#     i += 1
#
# #在cnt位置插入空格,涉及到python字符串更改的操作知识点(https://www.cnblogs.com/huangbiquan/p/7783057.html)！！！
# string = string[:cnt]+" "+string[cnt:]
# end = cnt
# while end <= cnt+len(target)+1:
#     if string[i] != " ":
#         end += 1
#     i += 1
#
# string = string[:end]+" "+string[end:]
# # print(string)
# # print(string[cnt:end])
# print(string)
# if " " in string[cnt:end]:
#     tmp = string[cnt:end].replace(" ","")
#     print(string[:cnt+1])
#     string = string[:cnt+1]+tmp+string[end:]
# print(string)
#
#
