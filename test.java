����ͰͿͷ�����Ա������n���ͷ�С�飬����ҪΪÿһ�鰲�ſͷ�24Сʱֵ�ࡣΪ�����������ÿ��ֻ��2���ͷ���һ��ֻ��Ҫ1���ͷ��ϰ࣬����һЩ�ͷ�����ĳЩԭ������ͬһ���ϰࡣ

�����Ѿ��Կͷ������˱�ţ���i��i>=1&&i<=n������Ŀͷ����Ϊ2*i-1��2*i������֪����m������Լ����ϵ���ͷ����a�Ϳͷ����b����һ���ϰࡣ

����Ա��Ҫ���������æ�жϽ����Ƿ���ڿ��еķ�����������m��Լ����ϵ��������ÿ���鶼��1���ͷ��ϰࡣ

���룺n(������n���飩

m(m��Լ����ϵ��������������m��
a,b(����a��b��λ�ͷ���Ų���ͬʱ�ϰ�)

������ж���û�п��з�����������������no������������yes

 

������

���룺
4
3
1,4
2,3
7,3

�����yes

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
	
	//���Զ�̬�滮������Ƚ��������һ���˰����ϸ�
	
	While(True):
	work_list = ()
		for mem in mem_list:
			work_list.append((mem.values())[0])
		//����г�ͻ���ȵ�������һ���Ա��
		//����޳�ͻ���н⣬����
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
		//�ٴ�Ѱ�ң����ͬ�������ظ���ͻ������False�޽�
		for limit in limit_list:
			if work_list.has(limit[0]) and work_list.has(limit[1]):
				key3 = mem_list.getkey(limit[0])
				key4 = mem_list.getkey(limit[1])
				break
		if key3 == key1 or key4 == key1:
			print('no solution')
			return False
		//�������ͬһ�����ظ���ͻ�������ӵ�һ������Ѱ��
		else:
			continue
}
���Զ����ֿ����������ϰ����������Ҫ���������ƹ���Щ�ϰ��ﵽ�յ��ȡ����
����������˴�����˶����յ���ʱ��̵�·���� ��֪������ֻ�����Ŷ���������ϱ������ƶ���
�ƶ����ٶ�Ϊ1m/s��������ÿת��90����Ҫ����1s��

 ���룺 
��һ�У����λ�����꼰�����˳����磺 
1 0 EAST
��������˳�ʼ����Ϊx=1,y=0���������泯���� 
�ڶ��У��յ�λ�����꼰�����˳����磺 
0 2 WEST
�����������Ҫ�ƶ�����x=0,y=2�����泯���� 
������������ǵ�ͼ�� 
��������������r,c�������е�ͼ�����ж�����������У��磺
2 3
0 1 0
0 0 0 
���У����Ͻ�Ϊ����ԭ�㣬��������Ϊx������ķ����Ƕ��������ϵ���Ϊy������ķ������Ϸ���
��ͼ��1�������ϰ�������˲���ǰ����0�������ϰ�������˿���ǰ�� ��ͼ�����ڵ�ÿ������֮��ľ���Ϊ1m��
0 <= l,w <= 128 
����� 
�����˴�����ƶ����յ�����Ҫ����������������ɴ�ʱ���65535

//��������ɵĵڶ�����Ŀ��ʱ�����ޣ�����ʹ��python�������û����ɱ�����˼·���������Ŀ����ʾ��л
def test(){
	init_x, init_y, init_direc = input('initial site and direction: ').split(' ')
	des_x, des_y, des_direc = input('destination site and direction').split(' ')
	//����������Ѿ��õ�һ����ͼ����,���ݽṹ����
	map = [ [], []]
	map = input('plz input the map:')
	
	//��������������������������
	time = 0
	diff_x = des_x - init_x
	diff_y = des_y - init_y
	
	//diff_x �� diff_y �������ֱ���ƻ������� �������� �� �ϱ������ת��
	
	//�Ƚ��к����ƶ���ÿ���ƶ�һ��֮�����¼���
	
}











