# standard_star
IFS 定标星场选取

背景及意
考虑到IFS光学系统性能、探测器响应、温度变化等因素，IFS测试定标环节将穿插覆盖其仪器研制及在轨服役全部阶段。 定标星场的选取直接影响到IFS在轨定标中辐射强度、光谱流量及波长、IFS及MCI视场位置等相关指标的精确性。

参考源（标准星表）及选
选源标准：
位置都分部在不同的地平高度的位置处；
颜色跨度/ Star type跨度大；
光谱特征明显/‘锐，深’（选取STIS推荐源）；
星等不能太暗
覆盖MCI / IFS视场（考虑几何定标）
......

分为三类：
=== 1. 辐射强度标准星： ===
Landolt 标准场（辐射强度标准星）

=== 2. 光谱标准星（以下星表中有一定程度交叉覆盖）： ===
HST Spectrophotometric Standards（光谱标准星）
STIS Spectrophotometric Standards（光谱标准星）
Oke1990；Hamuy et al1992; Massey1998. Spectrophotometric Standards （光谱标准星）


=== 3. 几何定标标准星 ===
M67 - MCI/IFS （几何标定星团）
47 Tuc
NGC6397
......


数据库的构建及Python包的调
=== 1. 标准星场数据库的建立（现有目录）： ===
辐射强度标准星：
Landolt1992

光谱标准星：
Massey1998
Hamuy1992
Oke1990


几何定标标准星团：
NGC6397
NGC6121
47Tuc_NGC104
NGC6540
NGC6752


=== 2. Python包的调用(debuging... 待进一步完善) ===
构建cal-star python 包，可以用 pip install cal-satr 命令安装。 具体参考 PyPI 及github 相关资源。 cal-star包含四个子函数：


sc_sp: 用于展示光谱定标星中的光谱流量相关信息；


sc_skymap: 光谱定标星空间二维分布（RA,DEC）等相关数据；


sc_photometry: 用于展示辐射强度定标星星表及空间二维分布（RA,DEC）相关信息；


sc_cluster: 用于展示几何定标星团的数据及 6 arcsec 的 zoom in 效果。


具体的函数调用参考demo.ipynb 及 demo2_cluster.ipynb 两个jupyter文件。 这两个文件被打包在'./cal-star/demo/'文件夹下,可以在 cal-star 安装路径下找到。

也在这里（demo,demo2 两个程序前半段程序没有采用cal-star包，后半段采用cal-star和前半段对比）：
https://github.com/git-yuliang/standard_star/tree/main/spec_cal/src/cal_star/demo
