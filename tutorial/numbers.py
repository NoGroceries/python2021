# Division (/) always returns a float
print(17 / 3)
print(17 // 3)  # 商
print(17 % 3)  # 余数
print(4 * 3.75 - 1)  # 混合类型时，会将int转换为float
# In interactive mode, the last printed expression is assigned to the variable _
# >>> 8/5
# 1.6
# >>> print(_)
# 1.6

# Python strings cannot be changed — they are immutable.
language = "Python"
print(language[0])
language[0] = 'J' # TypeError: 'str' object does not support item assignment
