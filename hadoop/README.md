## windows�� �ϵ� ��ġ�ϱ�

<p>

### 1. �غ�
VirtualBox-5.1.6-110634-Win.exe
<br>
�� VirtualBox ��ġ
<br>
C:\hadoop ������ �Ʒ� 5�� ���� �غ��س��´�.
</p>
<pre>
apache-hive-2.0.0-bin.tar.gz
CentOS-6.4-x86_64-bin-DVD1.iso
hadoop-2.7.2.tar.gz
jdk-7u80-linux-x64.tar.gz
protobuf-2.5.0.tar.gz
</pre>

<p>

### 2. ȯ�漳��
virtualbox ����> ȯ�漳��> �Է�> ����ӽ�> ȣ��Ʈ Ű ���� 
<br>

Ȯ�� Ȥ�� ����
<br>

ȯ�漳��> ��Ʈ��ũ> ȣ��Ʈ���� ��Ʈ��ũ> ������� ������> �����
<br>
���⿡ �ִ� IPv4�ּҴ� �� �����ӽ� �ȿ����� ���.
<br>
DHCP ����
<br>
������� üũ Ȯ��
<br>
�����ּ��Ѱ�~�ְ��ּ��Ѱ� ���̿����� ���
<br>
��Ȥ �浹�Ǹ� �� �ּ� �ȿ��� �ٲ㼭 ���� ��.
</p>


<p>

### 3. ���θ����(�����ڽ� ������ ��ư)
�̸��� hadoopserver �Է�
<br>
����: ������
<br>
����: Red Hat(64 bit)
<br>
�޸� ũ��: 1�Ⱑ ����(�ϴ���)
<br>
�ϵ��ũ: ���� �� ���� �ϵ� ��ũ �����
<br>
�ϵ��ũ ���� ����: VDI
<br>
����ũ��(�� �� ����)
<br>
���� ��ġ �� ũ��: 16�Ⱑ(�ϴ�)
<br>
����� Ŭ��
<br>
���� ������ hadoopserver�� ����.
</p>

<p>

### 4. ����
�Ϲ�> ���> Ŭ������ ����: �����/ �巡�׾ص��: �����
<br>
��Ʈ��ũ> �����2> ��Ʈ��ũ ����� ����ϱ� Ŭ��
<br>
<b>
������ �����: ȣ��Ʈ ���� �����
</b>
<br>
���������: ��� ���
<br>
���̺� ����� üũ���ִ°� Ȯ��
<br>
��������> ���� �߰� ������> 
<br>
���� ���: ��Ÿ Ŭ��, C:\hadoop ����, �ڵ� ����Ʈ Ŭ��, ok
<br>
</p>

<p>

### 5. ���� (�����ӽ� ���� ���� ��ư)
�õ���ũ ����
<br>
������ ���� ��� Ŭ��
<br>
centos iso ���� ����, ����, ����, ����
<br>
��ŵ
<br>
���� US English��
<br>
Yes
<br>
hostname: hadoopserver
<br>
Asia: Seoul
<br>
id/pw �Է�
<br>
desktop���� ����
<br>
customize add ����, developer> developer tool ��ġ
<br>
�����̸��� root(������,���н� ���۰����� �׻� root), pw�� pw��
<br>
terminal ��� ls, cd, (�ٽ�) ls
</p>
<pre>
<code>
ls -al
ll
cd
</code>
</pre>

### 6. ��Ʈ��ũ ����
<pre>
<code>
cd /etc/sysconfig/network-scripts
pwd
ls
(ifcfg-eth0, 1 �ִ��� Ȯ��)
cat ifcfg-eth0
cat ifcfg-eth1
(ifcfg-eth0�� onboot=no�� �̵��� yes�� �ٲ� ����)
(ifcfg-eth1�� onboot=no�� �̵��� yes�� �ٲٰ�, 
nm_controlled=yes�� ���ΰ�, 
bootproto=dhcp�� none���� �ٲٰ�, 
NETMASK=255.255.255.0 �߰�,
IPADDR=192.168.56.101 �߰�)
</code>
</pre>
<p>
ifcfg-eth1�� ������ vm�ȿ� ������ server�鳢�� ����ϱ� ���� �뵵
</p>

<pre>
<code>
vi ifcfg-eth0
����Ű�� ���ϴ� ��ġ�� ���� cw������ ������. �׸��� ���ϴ� Ű���� �Է�.

���� �Ʒ��ٷ� ������ 
G
�� �� �߰��Ϸ��� 
o
����ϰ� ���� ����
escŰ :q!
�����ϰ� ���� ����
escŰ :wq

(�����ϰ� ����)
service network restart
(���ͳ� �Ǵ��� Ȯ��)
cat /etc/hosts
vi /etc/hosts
</code>
</pre>





