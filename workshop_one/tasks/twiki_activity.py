
def get_user_info (l):
   act = {}
   for e in l:
        if e in act:
           act[e] += 1
        else:
           act[e] = 1
   return act

activity_d = {}
with open ('TWiki_Application.log', 'r') as f:
    for l in f:
        lines = l.split(' | ')
        if lines[1] in activity_d:
              activity_d[lines[1]].append(lines[2])
        else:
             activity_d[lines[1]] = [lines[2]]
            
print ('WinstonChurchill', get_user_info(activity_d['WinstonChurchill']))
print ('JawaharlalNehru', get_user_info(activity_d['JawaharlalNehru']))


