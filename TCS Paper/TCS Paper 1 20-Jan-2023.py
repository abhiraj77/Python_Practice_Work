# IPA 20th Jan 2023
# Paper 1

def str_num_list(inp):
    ans = []
    alpha = ''.join([i for i in inp if i.isalpha()])
    if len(alpha) != 0:
        ans.append(alpha)
    num = ''.join([i for i in inp if i.isdigit()])
    if len(num) != 0:
        ans.append(int(num))
    return ans

inp = ["Hyper12345Lower100","Sachin24Apr","LionelMessi","100210"]
for i in inp:
    ans = str_num_list(i)
    print(f"Input:{i}\nOutput:{ans}\n")