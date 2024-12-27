str1 = input();
str2 = input();

str1 = str1[1::2];
str1 +=str2[::2];

print(str1)