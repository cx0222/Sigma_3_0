import tkinter as tk
import tkinter.messagebox
import sympy
import PIL
from sympy import *
from tkinter import *
from tkinter import Menu
from PIL import Image, ImageTk

print('\n 三元轮换对称不等式运算程序\n')
print(' ver 2.6 [20210114]')
print(' *cx2020 Jinan, Shandong')

a, b, c = sympy.symbols('a, b, c')
s, t, d = sympy.symbols('s, t, d')
as_cs, as_sc, as_pqr, as_ast, ast, _same_ = False, False, False, False, True, False


def info():
    print(' 基于Python 3开发的 三元轮换对称不等式运算程序\n')
    print(' ----------------- Contact -----------------')
    print(' *cx2020 Jinan, Shandong')
    print(' 2913026224@qq.com\n')
    print(' ------------- Current Version -------------')
    print(' 该版本装载的核心算法版本 ver 2.5 和 2.6')
    print(' 该版本仅支持齐次不等式')
    print(' 该版本pqr分拆仅支持全对称不等式\n')
    print(' ------------- History Version -------------')
    print(' ver 2.5 [20210113] Jinan, Shandong')
    print(' ver 2.4 [20210111] Jinan, Shandong')
    print(' ver 2.3 [20210110] Jinan, Shandong')
    print(' ver 2.2 [20210105] Jinan, Shandong')
    print(' ver 2.1 [20210104] Jinan, Shandong')
    print(' ver 1.6 [20201229] Jinan, Shandong')
    print(' ver 1.5 [20201225] Jinan, Shandong')
    print(' ver 1.4 [20201223] Jinan, Shandong')
    print(' ver 1.3 [20201222] Jinan, Shandong')
    print(' ver 1.2 [20201221] Jinan, Shandong')
    print(' ver 1.1 [20201221] Jinan, Shandong\n')
    print(' ------ Recommended Version for Python -----')
    print(' Python 3.7.x or later with sympy\n')


def hint():
    print(' --------------- Instruction ---------------')
    print(' [功能一] normal0(expr)')
    print('  [说　明] 对三元三次齐次轮换对称不等式通分，并输出整理后的分子；')
    print('  [注意一] expr的类型是字符串，因此需要添加英文引号；')
    print('  [注意二] 本函数会首先对表达式求和，即对表达式加上 Σ（轮换和）符号，通分后提取分子部分.\n')
    print(' [功能二] cs2_5(expr)')
    print('  [说明一] 对三元齐次轮换对称不等式作SOS分拆；')
    print('  [说明二] 对三元轮换对称不等式作SOS分拆得到通式后，再输出一个易于展示的形式；')
    print('  [注意一] expr的类型是字符串，因此需要添加英文引号；')
    print('  [注意二] 本函数会首先对表达式求和，即对表达式加上 Σ（轮换和）符号，通分后提取分子部分；')
    print('  [注意三] 有多种SOS分拆结果时，会将通式参数化表示（v[i]a）.\n')
    print(' [功能三] sc2_5(expr)')
    print('  [说明一] 对三元齐次轮换对称不等式作Schur分拆；')
    print('  [说明二] 对三元轮换对称不等式作Schur分拆得到通式后，再输出一个易于展示的形式；')
    print('  [注意一] expr的类型是字符串，因此需要添加英文引号；')
    print('  [注意二] 本函数会首先对表达式求和，即对表达式加上 Σ（轮换和）符号，通分后提取分子部分；')
    print('  [注意三] 有多种Schur分拆结果时，会将通式参数化表示（v[i]a）.\n')
    print(' [功能四] ast2_5(expr)')
    print('  [说明一] 对三元齐次轮换对称不等式通分，并对整理后的分子作差分代换；')
    print('  [说明二] 令 (a, b, c) ➡ (a, a + s, a + t)；')
    print('  [注意一] expr的类型是字符串，因此需要添加英文引号；')
    print('  [注意二] 本函数会首先对表达式求和，即对表达式加上 Σ（轮换和）符号，通分后提取分子部分.\n')


def ex_0(expr):
    expr0 = [i for i in expr]
    exprnewa = ''
    for i in range(0, expr0.__len__()):
        if expr0[i] == 'a':
            expr0[i] = 'b'
            continue
        if expr0[i] == 'b':
            expr0[i] = 'c'
            continue
        if expr0[i] == 'c':
            expr0[i] = 'a'
            continue
    for i in range(0, expr0.__len__()):
        exprnewa += expr0[i]
    exprnewa = str(exprnewa)
    return exprnewa


def ex_1(expr):
    expr0 = [i for i in expr]
    exprnewb = ''
    for i in range(0, expr0.__len__()):
        if expr0[i] == 'a':
            expr0[i] = 'c'
            continue
        if expr0[i] == 'b':
            expr0[i] = 'a'
            continue
        if expr0[i] == 'c':
            expr0[i] = 'b'
            continue
    for i in range(0, expr0.__len__()):
        exprnewb += expr0[i]
    exprnewb = str(exprnewb)
    return exprnewb


def sigma(expr):
    exprnew = ex_0(expr) + ' + ' + ex_1(expr) + ' + ' + expr
    exprnew = str(exprnew)
    return exprnew


def pi(expr):
    exprnew = '(' + ex_0(expr) + ') * (' + ex_1(expr) + ') * (' + expr + ')'
    exprnew = str(exprnew)
    return exprnew


def judge1(expr):
    expr1 = sympy.simplify(numer(cancel(sigma(expr))))
    deg0 = Poly(expr1, a, b, c).total_degree()
    return deg0


def normal0(expr):
    expr0 = sympy.simplify(numer(cancel(sigma(expr))))
    return expr0


def normal1(expr):
    expr0 = sympy.simplify(numer(cancel(expr)))
    return expr0


def cs2_5(expr):
    if as_cs:
        print('[整理] ', normal0(expr))
        expr0 = str(numer(cancel(sigma(expr))))
        expr2 = numer(cancel(sigma(expr)))
    else:
        print('[整理] ', normal1(expr))
        expr0 = str(numer(cancel(expr)))
        expr2 = numer(cancel(expr))
    s_bc, s_ca, s_ab = (b - c) ** 2, (c - a) ** 2, (a - b) ** 2
    deg0 = judge1(expr0)
    fnum = dict1(deg0).__len__()
    varlistf = sympy.symbols('v:{}:a'.format(fnum))
    s_a, s_b, s_c = 0, 0, 0
    for i in range(0, fnum):
        s_a += varlistf[i] * dict1(deg0)[i]
        s_b += varlistf[i] * sympy.simplify(ex_0('{0}'.format(dict1(deg0)[i])))
        s_c += varlistf[i] * sympy.simplify(ex_1('{0}'.format(dict1(deg0)[i])))
    ineq = s_a * s_bc + s_b * s_ca + s_c * s_ab
    ineq0 = expand(s_a * s_bc + s_b * s_ca + s_c * s_ab)
    func0 = sympy.poly(ineq0 - expr2, a, b, c)
    equlist0 = []
    for i in range(0, dict0(deg0).__len__()):
        equlist0.append(func0.coeff_monomial(dict0(deg0)[i]))
    ans = solve(equlist0, varlistf)
    result0 = ineq.subs(ans)
    result2_a, result2_b, result2_c = s_a.subs(ans), s_b.subs(ans), s_c.subs(ans)
    result0 = str(result0)
    varlistf0 = [str(varlistf[i]) for i in range(0, fnum)]
    varlistf1, i = [], 0
    result2 = s_a.subs(ans)
    for j in range(0, fnum):
        if varlistf0[j] in result0:
            varlistf1.append(varlistf0[j])
    fnum0 = varlistf1.__len__()
    if fnum0 == 0:
        print('[结果] ', 'Σ ({0}) * (b - c) ** 2'.format(result2))
    else:
        print('[通式] ', 'Σ ({0}) * (b - c) ** 2'.format(result2))
        varlistf2 = [[] for i in range(0, fnum0)]
        for k in range(0, fnum0):
            varlistf2[k] = sympy.symbols(varlistf1[k])
        varlistf3 = [varlistf2[i] for i in range(0, fnum0)]
        print('[参数] ', varlistf2)
        if judge1(expr0) == 4:
            add_a = sympy.poly(result2_a, a, b, c)
            equlist_4_1 = [add_a.coeff_monomial(c ** 2) - add_a.coeff_monomial(a ** 2)]
            equlist_4_2 = [add_a.coeff_monomial(a ** 2) - add_a.coeff_monomial(b ** 2)]
            add0_4 = solve(equlist_4_1 + equlist_4_2, varlistf3)
            result2 = numer(factor(add_a.subs(add0_4)))
            print('[默认] ', 'Σ ({0}) * (b - c) ** 2'.format(result2))
        if judge1(expr0) >= 5:
            add_a = sympy.poly(result2_a, a, b, c)
            add0_5 = {varlistf2[i]: 1 for i in range(0, fnum0)}
            result2 = numer(factor(add_a.subs(add0_5)))
            print('[默认] ', 'Σ ({0}) * (b - c) ** 2'.format(result2))


def sc2_5(expr):
    if as_sc:
        print('[整理] ', normal0(expr))
        expr0 = str(numer(cancel(sigma(expr))))
        expr2 = numer(cancel(sigma(expr)))
    else:
        print('[整理] ', normal1(expr))
        expr0 = str(numer(cancel(expr)))
        expr2 = numer(cancel(expr))
    s_bc, s_ca, s_ab = (a - b) * (a - c), (b - c) * (b - a), (c - a) * (c - b)
    deg0 = judge1(expr0)
    fnum = dict1(deg0).__len__()
    varlistf = sympy.symbols('v:{}:a'.format(fnum))
    s_a, s_b, s_c = 0, 0, 0
    for i in range(0, fnum):
        s_a += varlistf[i] * dict1(deg0)[i]
        s_b += varlistf[i] * sympy.simplify(ex_0('{0}'.format(dict1(deg0)[i])))
        s_c += varlistf[i] * sympy.simplify(ex_1('{0}'.format(dict1(deg0)[i])))
    ineq = s_a * s_bc + s_b * s_ca + s_c * s_ab
    ineq0 = expand(s_a * s_bc + s_b * s_ca + s_c * s_ab)
    func0 = sympy.poly(ineq0 - expr2, a, b, c)
    equlist0 = []
    for i in range(0, dict0(deg0).__len__()):
        equlist0.append(func0.coeff_monomial(dict0(deg0)[i]))
    ans = solve(equlist0, varlistf)
    result0 = ineq.subs(ans)
    result2_a, result2_b, result2_c = s_a.subs(ans), s_b.subs(ans), s_c.subs(ans)
    result0 = str(result0)
    varlistf0 = [str(varlistf[i]) for i in range(0, fnum)]
    varlistf1, i = [], 0
    result2 = s_a.subs(ans)
    for j in range(0, fnum):
        if varlistf0[j] in result0:
            varlistf1.append(varlistf0[j])
    fnum0 = varlistf1.__len__()
    if fnum0 == 0:
        print('[结果] ', 'Σ ({0}) * (a - b) * (a - c)'.format(result2))
    else:
        print('[通式] ', 'Σ ({0}) * (a - b) * (a - c)'.format(result2))
        varlistf2 = [[] for i in range(0, fnum0)]
        for k in range(0, fnum0):
            varlistf2[k] = sympy.symbols(varlistf1[k])
        varlistf3 = [varlistf2[i] for i in range(0, fnum0)]
        print('[参数] ', varlistf2)
        if judge1(expr0) == 4:
            add_a = sympy.poly(result2_a, a, b, c)
            equlist_4_1 = [add_a.coeff_monomial(c ** 2) - add_a.coeff_monomial(a ** 2)]
            equlist_4_2 = [add_a.coeff_monomial(a ** 2) - add_a.coeff_monomial(b ** 2)]
            add0_4 = solve(equlist_4_1 + equlist_4_2, varlistf3)
            result2 = numer(factor(add_a.subs(add0_4)))
            print('[默认] ', 'Σ ({0}) * (a - b) * (a - c)'.format(result2))
        if judge1(expr0) >= 5:
            add_a = sympy.poly(result2_a, a, b, c)
            add0_5 = {varlistf2[i]: 1 for i in range(0, fnum0)}
            result2 = numer(factor(add_a.subs(add0_5)))
            print('[默认] ', 'Σ ({0}) * (a - b) * (a - c)'.format(result2))


def pqr2_6(expr):
    if _same_:
        result2_6_1 = pqr2_6_1(expr)
        return result2_6_1
    else:
        result2_6_2 = pqr2_6_2(expr)
        return result2_6_2


def pqr2_6_1(expr):
    if as_pqr:
        ineq0 = numer(cancel(sigma(expr)))
    else:
        ineq0 = numer(cancel(expr))
    a, b, c = sympy.symbols('a, b, c')
    p, q, r = sympy.symbols('p, q, r')
    list1, list2, equlist0 = [], dict0(judge1(expr)), []
    list0 = dict2(judge1(expr))[-1]
    fnum0, fnum1, result0, resultpqr = list0.__len__(), list2.__len__(), 0, 0
    varlistf = sympy.symbols('c:{}:a'.format(fnum0))
    for i in range(0, fnum0):
        list1.append(list0[i].subs({p: (a + b + c), q: a * b + b * c + c * a, r: a * b * c}))
        result0 += list1[i] * varlistf[i]
        resultpqr += list0[i] * varlistf[i]
    result1 = sympy.poly(sympy.simplify(result0) - ineq0, a, b, c)
    for i in range(0, fnum1):
        equlist0.append(result1.coeff_monomial(list2[i]))
    ans = solve(equlist0, varlistf)
    result2 = factor(resultpqr.subs(ans))
    return result2


def pqr2_6_2(expr):
    if as_pqr:
        ineq0 = numer(cancel(sigma(expr)))
    else:
        ineq0 = numer(cancel(expr))
    a, b, c = sympy.symbols('a, b, c')
    p, q, r = sympy.symbols('p, q, r')
    deg0 = judge1(expr)
    poly0 = sympy.poly(ineq0, a, b, c)
    polydict0 = poly0.as_dict()
    all0 = list(zip(list(polydict0.keys()), list(polydict0.values())))
    length0 = all0.__len__()
    listcy = [[] for cy in range(0, deg0 + 1)]
    listcy0 = [0 * a for cy in range(0, deg0 + 1)]
    for cy in range(1, deg0 + 1):
        for len in range(0, length0):
            if sum(all0[len][0]) == cy:
                listcy[cy].append(
                    (a ** all0[len][0][0] * b ** all0[len][0][1] * c ** all0[len][0][2]) * all0[len][1])
        count0 = listcy[cy].__len__()
        for i in range(0, count0):
            listcy0[cy] += listcy[cy][i]
        listcy0[cy] = sympy.simplify(listcy0[cy])
    for len in range(0, length0):
        if sum(all0[len][0]) == 0:
            listcy0[0] = all0[len][1]
    result3 = listcy0[0]
    for i in range(1, deg0 + 1):
        if as_pqr:
            result3 += pqr2_6_1(str(listcy0[i])) / 3
        else:
            result3 += pqr2_6_1(str(listcy0[i]))
    return result3


def ast2_5(expr):
    if as_ast:
        exprast = str(normal0(str(expr)))
    else:
        exprast = str(normal1(str(expr)))
    expr0, expr1 = [i for i in exprast], ''
    for i in range(0, expr0.__len__()):
        if expr0[i] == 'b':
            expr0[i] = '(a+s)'
            continue
        if expr0[i] == 'c':
            if ast:
                expr0[i] = '(a+t)'
                continue
            else:
                expr0[i] = '(a+s+t)'
    for i in range(0, expr0.__len__()):
        expr1 += expr0[i]
    expr1 = collect(sympy.simplify(expand(expr1)), a)
    return expr1


def dict0(jud0):
    termlist0 = []
    for i in range(0, jud0 + 1):
        for j in range(0, jud0 + 1):
            for k in range(0, jud0 + 1):
                if i + j + k == jud0:
                    termlist0.append(a ** i * b ** j * c ** k)
    return termlist0


def dict1(jud1):
    termlist1 = []
    for i in range(0, jud1 - 1):
        for j in range(0, jud1 - 1):
            for k in range(0, jud1 - 1):
                if i + j + k == jud1 - 2:
                    termlist1.append(a ** i * b ** j * c ** k)
    return termlist1


def dict2(deg0):
    pqrdict = [[] for k in range(0, deg0 + 1)]
    p, q, r = sympy.symbols('p, q, r')
    for d in range(0, deg0 + 1):
        for p0 in range(0, d + 1):
            for q0 in range(0, d + 1):
                for r0 in range(0, d + 1):
                    if p0 + 2 * q0 + 3 * r0 == d:
                        pqrdict[d].append(p ** p0 * q ** q0 * r ** r0)
    return pqrdict


def getcs():
    exp0 = entry0.get()
    print('\n[输入] ', exp0)
    cs2_5(exp0)
    tk.messagebox.showinfo('提示', 'SOS分拆已完成！')


def getsc():
    exp0 = entry0.get()
    print('\n[输入] ', exp0)
    sc2_5(exp0)
    tk.messagebox.showinfo('提示', 'Schur分拆已完成！')


def getpqr():
    exp0 = entry0.get()
    print('\n[输入] ', exp0)
    if as_pqr:
        print('[整理] ', normal0(exp0))
    else:
        print('[整理] ', normal1(exp0))
    print('[换元]  (a + b + c, a*b + b*c + c*a, a*b*c) ⬅ (p, q, r)')
    print('[结果] ', pqr2_6(exp0))
    tk.messagebox.showinfo('提示', 'pqr分拆已完成！')


def getast():
    exp0 = entry0.get()
    print('\n[输入] ', exp0)
    if as_ast:
        print('[整理] ', normal0(exp0))
    else:
        print('[整理] ', normal1(exp0))
    print('[换元]  (a, a + s, a + t) ⬅ (a, b, c)')
    print('[结果] ', ast2_5(exp0))
    tk.messagebox.showinfo('提示', '差分代换已完成！')


def _true_(func):
    global as_cs, as_sc, as_pqr, as_ast, ast, _same_
    if func == 1:
        as_cs = not as_cs
    if func == 2:
        as_sc = not as_sc
    if func == 3:
        as_pqr = not as_pqr
    if func == 4:
        as_ast = not as_ast
    if func == 5:
        ast = not ast
    if func == 6:
        _same_ = not _same_


def _exit_():
    window0.quit()
    window0.destroy()
    exit()


def _about_():
    window1 = tk.Toplevel()
    window1.geometry('800x400')
    window1.resizable(False, False)
    bg0 = ImageTk.PhotoImage(Image.open('ver 2_6.gif'))
    canvas0 = tk.Canvas(window1, width=800, height=400, bg='white')
    canvas0.create_image(400, 200, image=bg0)
    canvas0.pack()
    window1.mainloop()


def _all_():
    hint()
    info()


window0 = tk.Tk()
window0.title('三元轮换对称不等式运算程序  ver 2.6 [20210114]')
window0.geometry('800x400')
window0.resizable(False, False)
title0 = tk.Label(window0,
                  text='\n基于Python 3开发的 三元轮换对称不等式运算程序\n ver 2.6 [20210114]  *cx2020 Jinan, Shandong',
                  font=('Arial', 18))
title1 = tk.Label(window0,
                  text='请以a, b, c作为不等式的变量',
                  font=('Arial', 13))
menu0 = tk.Menu(window0)
window0.config(menu=menu0)
menu_operate = tk.Menu(menu0, tearoff=False)
menu_operate.add_command(label='SOS分拆', command=getcs)
menu_operate.add_command(label='Schur分拆', command=getsc)
menu_operate.add_command(label='pqr分拆', command=getpqr)
menu_operate.add_command(label='差分代换', command=getast)
menu_operate.add_separator()
menu_operate.add_command(label='Exit...', command=_exit_)
menu0.add_cascade(label='Operation', menu=menu_operate)
menu_help = tk.Menu(menu0, tearoff=False)
menu_help.add_command(label='About...', command=_about_)
menu_help.add_command(label='More information...', command=_all_)
menu0.add_cascade(label='Help', menu=menu_help)
about0 = tk.Button(window0, text='关于', command=_about_)
entry0 = tk.Entry(window0, width=80)
cs0 = tk.Button(window0, text="SOS分拆", command=getcs)
sc0 = tk.Button(window0, text="Schur分拆", command=getsc)
pqr0 = tk.Button(window0, text="pqr分拆", command=getpqr)
ast0 = tk.Button(window0, text="差分代换", command=getast)
exit0 = tk.Button(window0, text="退出", command=_exit_)
cs1 = tk.Checkbutton(window0, text='自动求和', command=lambda: _true_(1))
sc1 = tk.Checkbutton(window0, text='自动求和', command=lambda: _true_(2))
pqr1 = tk.Checkbutton(window0, text='自动求和', command=lambda: _true_(3))
pqr2 = tk.Checkbutton(window0, text='是否为齐次不等式', command=lambda: _true_(6))
ast1 = tk.Checkbutton(window0, text='自动求和', command=lambda: _true_(4))
ast2 = tk.Checkbutton(window0, text='(a, a + s, a + s + t)', command=lambda: _true_(5))
title0.pack(), about0.pack(), entry0.pack(), title1.pack()
cs0.pack(), cs1.pack(), sc0.pack(), sc1.pack()
pqr0.pack(), pqr1.pack(), pqr2.pack(), ast0.pack(), ast1.pack(), ast2.pack()
exit0.pack(), window0.mainloop()
