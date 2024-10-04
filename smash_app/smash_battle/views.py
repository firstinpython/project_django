# from django.shortcuts import render
#
# # Create your views here.
# from django.shortcuts import render
# # import smash_users.models
# import random
# import smash_db.models
#
# # Create your views here.
# full_people_bd = smash_db.models.Smash_Users_Model.objects.all()
# mass_username = []
#
# for item in full_people_bd:
#     if item.tag:
#         mass_username.append(item.tag)
# maxx = 0
# word = ''
# for tags in mass_username:
#     if len(tags) > maxx:
#         maxx = len(tags)
#         word = tags
# print(maxx, word)
# mass_users_cart = [random.choice(mass_username) for j in range(2)]
# mass_context_users = []
# mass_username.remove(mass_users_cart[0])
# mass_username.remove(mass_users_cart[1])
#
#
# def comp_people(request):
#     global mass_context_users
#     if request.method == "POST":
#         tag = request.POST['tag']
#         page_user1 = mass_context_users[0]
#         page_user2 = mass_context_users[1]
#         if tag != page_user1.tag:
#             page_user1.battle_like_activity = 0
#             page_user2.battle_like += 1
#             ind_user1 = mass_context_users.index(page_user1)
#             mass_context_users.pop(ind_user1)
#             mass_username.append(page_user1.tag)
#             context_user_tag = [random.choice(mass_username) for i in range(1)]
#             mass_context_users.append(smash_db.models.Smash_Users_Model.objects.get(tag=context_user_tag[0]))
#         elif tag != page_user2.tag:
#             page_user2.battle_like_activity = 0
#             page_user1.battle_like += 1
#             ind_user2 = mass_context_users.index(page_user2)
#             mass_context_users.pop(ind_user2)
#             mass_username.append(page_user2.tag)
#             context_user_tag = [random.choice(mass_username) for i in range(1)]
#             mass_context_users.append(smash_db.models.Smash_Users_Model.objects.get(tag=context_user_tag[0]))
#         page_user1.save()
#         page_user2.save()
#         print(mass_context_users)
#         context = {
#             'users': mass_context_users
#         }
#         return render(request, 'smash_battle/index.html', context=context)
#
#     for users_cart in mass_users_cart:
#         users = smash_db.models.Smash_Users_Model.objects.get(tag=users_cart)
#         users.battle_like_activity = 1
#         mass_context_users.append(users)
#
#     print(mass_context_users)
#     context = {
#         'users': mass_context_users
#     }
#     return render(request, 'smash_battle/index.html', context=context)
