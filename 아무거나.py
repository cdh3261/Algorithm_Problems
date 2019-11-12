import sys
sys.stdin = open('./SWTEST/점심식사시간.txt','r')

for tc in range(int(input())):
   N = int(input())
   room = [list(map(int, input().split())) for _ in range(N)]
   room_loc = []
   stair = []
    # 방좌표,룸좌표
   for i in range(N):
       loc_tmp = []
       stair_tmp = []
       for j in range(N):
           if room[i][j] == 1:
               loc_tmp.append(i)
               loc_tmp.append(j)
               room_loc.append(loc_tmp)
               loc_tmp = []
           elif room[i][j] > 1:
               stair_tmp.append(i)
               stair_tmp.append(j)
               stair.append(stair_tmp)
               stair_tmp = []

    # 조합
   way1 = []
   way2 = []
   for i in range(1 << len(room_loc)):
       tmp1 = []
       tmp2 = []
       for j in range(len(room_loc)):

           if i & (1 << j) != 0:

               tmp1.append(room_loc[j])
           else:
               tmp2.append(room_loc[j])

       way1.append(tmp1)
       way2.append(tmp2)

    # 거리
   road1 = []
   road2 = []
   for i in range(len(way1)):
       road_tmp = []
       road_tmp2 = []
       for j in range(len(way1[i])):
           road_tmp.append(abs(way1[i][j][0] - stair[0][0]) + abs(way1[i][j][1] - stair[0][1]))
       if road_tmp != []:
           road1.append(sorted(road_tmp))
       else:
           road1.append([0])
       for x in range(len(way2[i])):
           road_tmp2.append(abs(way2[i][x][0] - stair[1][0]) + abs(way2[i][x][1] - stair[1][1]))
       if road_tmp2 != []:
           road2.append(sorted(road_tmp2))
       else:
           road2.append([0])
   for i in range(len(way1)):
       road_tmp = []
       road_tmp2 = []
       for j in range(len(way1[i])):
           road_tmp.append(abs(way1[i][j][0]-stair[1][0])+abs(way1[i][j][1]-stair[1][1]))
       if road_tmp != []:
           road1.append(sorted(road_tmp))
       else:
           road1.append([0])
       for x in range(len(way2[i])):
           road_tmp2.append(abs(way2[i][x][0]-stair[0][0])+abs(way2[i][x][1]-stair[0][1]))
       if road_tmp2 != []:
           road2.append(sorted(road_tmp2))
       else:
           road2.append([0])

   Vmax = 99999

   for i in range(len(road1)):

       if len(road1[i]) <= 3:
           if road1[i][0] == 0:
               a = 0
           else:
               a = road1[i][-1]+room[stair[0][0]][stair[0][1]]+1

       else:
           for z in range(len(road1[i])):
               if z >= 3:
                   if road1[i][z-3]+room[stair[0][0]][stair[0][1]] > road1[i][z]:
                       a = road1[i][z]+1+road1[i][z-3]+room[stair[0][0]][stair[0][1]]+1
                       road1[i][z] = a
                   else:
                       a = road1[i][-1]+room[stair[0][0]][stair[0][1]]+1
                       road1[i][z] = a


       if len(road2[i]) <= 3:
           if road2[i][0] == 0:
               b = 0
           else:
               b = road2[i][-1]+room[stair[1][0]][stair[1][1]]+1

       else:
           for z in range(len(road2[i])):
               if z >= 3:
                   if road2[i][z-3]+room[stair[1][0]][stair[1][1]] > road2[i][z]:
                       b = road2[i][z]+1 + road2[i][z-3]+room[stair[1][0]][stair[1][1]]+1
                       road2[i][z] = b
                   else:
                       b = road2[i][z]+room[stair[1][0]][stair[1][1]]+1+1
                       road2[i][z] = b


       tmp3 = max(a, b)
       if Vmax > tmp3:
           Vmax = tmp3

           # print(road1[i])
           # print(road2[i])
   print(Vmax)