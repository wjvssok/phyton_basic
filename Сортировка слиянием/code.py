#ввод строки, содержащей список, например "[5, 2, 13]"
fst_list = input()
sec_list = input()

if fst_list == "":
    print("Строка пустая")
    sec_list = eval(sec_list)
    print(sorted(sec_list))
    
if sec_list == "":
    print("Строка пустая")
    fst_list = eval(fst_list)
    print(sorted(fst_list))

else :
  fst_list = eval(fst_list)
  sec_list = eval(sec_list)
  novyi_list = fst_list + sec_list
  sorted_list = sorted(novyi_list)
  print(sorted_list)