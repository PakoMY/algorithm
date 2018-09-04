阿里巴巴客服管理员管理着n个客服小组，他需要为每一组安排客服24小时值班。为简单起见，假设每组只有2个客服，一天只需要1个客服上班，并且一些客服由于某些原因不能在同一天上班。

我们已经对客服进行了编号，第i（i>=1&&i<=n）个组的客服编号为2*i-1和2*i。并且知道了m种如下约束关系：客服编号a和客服编号b不能一起上班。

管理员需要聪明的你帮忙判断今天是否存在可行的方案，既满足m条约束关系，又能让每个组都有1个客服上班。

输入：n(代表有n个组）

m(m条约束关系），接下来会有m行
a,b(代表a，b两位客服标号不能同时上班)

输出：判断有没有可行方案：如果不可行输出no；如果可行输出yes

 

举例：

输入：
4
3
1,4
2,3
7,3

输出：yes

import sys
def test(){
	group_num = input('group num:')
	limit_num = input('limit num:')
	mem_list = {}
	limit_list = ()
	
	
	for i in range(1, int(group_num)+1):
		mem_list.append(i :(2*i, 2*i -1))
	
	for i in range(int(limit_num)):
		x, y = input('limit:').split(',')
		limit_list.append((x, y))
	
	//尝试动态规划解决，先将所有组第一个人安排上岗
	
	While(True):
	work_list = ()
		for mem in mem_list:
			work_list.append((mem.values())[0])
		//如果有冲突，先调整其中一组的员工
		//如果无冲突，有解，结束
		for limit in limit_list:
			if work_list.has(limit[0]) and work_list.has(limit[1]):
				key1 = mem_list.getkey(limit[0])
				key2 = mem_list.getkey(limit[1])
				break
			if limit == limit.last():
				print('There is a solution')
				return True
		work_list.remove(mem_list[key1][0])
		work_list.append(mem_list[key1][1])
		//再次寻找，如果同样的组重复冲突，返回False无解
		for limit in limit_list:
			if work_list.has(limit[0]) and work_list.has(limit[1]):
				key3 = mem_list.getkey(limit[0])
				key4 = mem_list.getkey(limit[1])
				break
		if key3 == key1 or key4 == key1:
			print('no solution')
			return False
		//如果不是同一个组重复冲突，继续从第一步进行寻找
		else:
			continue
}
在自动化仓库中有若干障碍物，机器人需要从起点出发绕过这些障碍物到终点搬取货柜，
现试求机器人从起点运动到终点用时最短的路径。 已知机器人只能沿着东西方向或南北方向移动，
移动的速度为1m/s，机器人每转向90度需要花费1s。

 输入： 
第一行：起点位置坐标及机器人朝向，如： 
1 0 EAST
代表机器人初始坐标为x=1,y=0，机器人面朝东方 
第二行：终点位置坐标及机器人朝向，如： 
0 2 WEST
代表机器人需要移动至点x=0,y=2，且面朝西方 
接下来输入的是地图： 
首先是两个数字r,c，代表有地图数据有多少行与多少列，如：
2 3
0 1 0
0 0 0 
其中，左上角为坐标原点，从左向右为x轴增大的方向是东方，从上到下为y轴增大的方向是南方。
地图中1代表有障碍物，机器人不能前往，0代表无障碍物机器人可以前往 地图中相邻的每两个点之间的距离为1m。
0 <= l,w <= 128 
输出： 
机器人从起点移动到终点所需要的最短秒数，当不可达时输出65535

//个人先完成的第二道题目，时间有限，个人使用python尝试求解没有完成表述了思路，如果被过目，表示感谢
def test(){
	init_x, init_y, init_direc = input('initial site and direction: ').split(' ')
	des_x, des_y, des_direc = input('destination site and direction').split(' ')
	//假如输入后已经得到一个地图矩阵,数据结构如下
	map = [ [], []]
	map = input('plz input the map:')
	
	//尝试利用深度优先搜索进行求解
	time = 0
	diff_x = des_x - init_x
	diff_y = des_y - init_y
	
	//diff_x 和 diff_y 的正负分别控制机器人在 东西方向 和 南北方向的转向
	
	//先进行横向移动，每次移动一次之后重新计算
	
}











