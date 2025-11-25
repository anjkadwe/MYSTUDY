
# dic = {
#  "name" : " anjalikadwe",
#  "age" : 23 ,
#   "lis" : [ 23 ,45,12,65],
 
# }

# print(dic)

# # print (dic["name"])
# print (dic["age"])
# print (dic["name"])

# dic["man"]= " mahesh"
# print(dic)
# print(type(dic))


#nested dictioner==============

# dic = {
#  "name" : " anjalikadwe",
#  "age" : 23 ,
#   "lis" : [ 23 ,45,12,65],
#   "nest_dic":{
#       "math": 23,
#       "phy": 45,
#       "sci":56,
#   }
# }

# print( dic["nest_dic"] )
# print( dic["nest_dic"] ["phy"])
# print( dic["lis"] )

# ============
# s = dic["lis"]                          none value
# print(s.sort()  )
# # =========

# dic = {
#  "name" : " anjalikadwe",
#  "age" : 23 ,
#   "lis" : [ 23 ,45,12,65],
#   "nest_dic":{
#       "math": 23,
#       "phy": 45,
#       "sci":56,
#   }
# }
# =====================method ========
#dic.keys() , dic.value() ,dic.items()


# # a= dic.update("me" ,"anju")
# a={"me" :"anju"}
# dic.update(a)
# print ( dic)

# # print(dic.get( "age"))

# print(dic.get( "nest_dic"))
# print(dic["age"])


# print( dic.items())

# print(dic.values())

# a = dic["nest_dic"]["phy"]=3
# print(dic.values())

# print(a )
# print(dic.values())



# print(dic.keys())
# print(type(dic.keys()))

# # a = list( dic.keys())
# # print(a)

# a = set( dic.keys())
# print(a)

# a = tuple( dic.keys())
# print(a)

# b= ( dic.keys())

# print(b)


#============================ set=============================

# set1={1,2,3,4,2,5,4}
# print( type( set1))
# print(set1)
# print(len(set1))

# set1.remove(2)
# set1.clear()
# set1.pop()
# set1.add( "anjali")
# # print( set1.add( "anjali"))          #none
# print(set1)

# g= set()

# print(type(g))


# set2= { "anj" ,5,4, "sub" ,"manho"}
# set1={ "manho" ,1,2,3,4,2,5,4}

# print(set1.union(set2))
# print(set2.union(set1))

# print( set1.intersection(set2))

 
# dic={}
# dic["table"] = {"gh"}

# print( dic)

# dic={}
# sub1= input( " sub1")
# sub2= input( " sub1")
# sub3= input( " sub1")

# dic["math"]=sub1
# dic["th"]=sub2
# dic["ath"]=sub3

# print(dic)

ser1 = {9}
s= {9.0}
print(float(s))
print(ser1.union(s))