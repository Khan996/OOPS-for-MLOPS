from oops_proj import chatbook

user1 = chatbook()
print(user1.id)

user2 = chatbook()
print(user2.id)


chatbook.set_id (10)
user3 = chatbook()
print(user3.id)

user4 = chatbook()
print(user4.id)



#user1 = chatbook()
#print(user1.id)

#user2 = chatbook()
#print(user2.id)

#user3 = chatbook()
#print(user3.id)




#print(user1.name)
#print(user1._chatbook__name)

# getter and setter
#print(user1.get_name())
#user1.set_name("Michael")
#print(user1.get_name())