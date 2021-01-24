import sympy
from sympy import *

print('\n 三元轮换对称不等式运算程序 for Python 3\n')
print(' ver 1.6 [20201229]')
print(' *cx2020 Jinan, Shandong')
print(' Type info() for more information\n'
      ' Type hint() for hints')

a, b, c = sympy.symbols('a, b, c')
x, y, z = sympy.symbols('x, y, z')
s, t, d = sympy.symbols('s, t, d')
a12, a13, a21, a23, a31, a32 = sympy.symbols('a12, a13, a21, a23, a31, a32')


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
        if expr0[i] == 'x':
            expr0[i] = 'y'
            continue
        if expr0[i] == 'y':
            expr0[i] = 'z'
            continue
        if expr0[i] == 'z':
            expr0[i] = 'x'
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
        if expr0[i] == 'x':
            expr0[i] = 'z'
            continue
        if expr0[i] == 'y':
            expr0[i] = 'x'
            continue
        if expr0[i] == 'z':
            expr0[i] = 'y'
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


def ast1_5(expr):
    exprast = str(normal0(str(expr)))
    expr0, expr1 = [i for i in exprast], ''
    for i in range(0, expr0.__len__()):
        if expr0[i] == 'b':
            expr0[i] = '(a+s)'
            continue
        if expr0[i] == 'c':
            expr0[i] = '(a+t)'
            continue
        if expr0[i] == 'y':
            expr0[i] = '(x+s)'
            continue
        if expr0[i] == 'z':
            expr0[i] = '(x+t)'
            continue
    for i in range(0, expr0.__len__()):
        expr1 += expr0[i]
    if judge0(expr) == 0:
        expr1 = collect(sympy.simplify(expand(expr1)), a)
    if judge0(expr) == 1:
        expr1 = collect(sympy.simplify(expand(expr1)), x)
    return expr1


def judge0(expr):
    if 'a' in expr and 'x' not in expr:
        form = 0
        return form
    if 'x' in expr and 'a' not in expr:
        form = 1
        return form
    if 'a' in expr and 'x' in expr:
        form = 2
        return form


def judge1(expr):
    expr1 = sympy.simplify(numer(cancel(sigma(expr))))
    deg0 = Poly(expr1, a, b, c).total_degree()
    return deg0


def normal0(expr):
    expr0 = sympy.simplify(numer(cancel(sigma(expr))))
    return expr0


def cs1_5(expr):
    print('[整理] ', normal0(expr))
    expr0 = str(numer(cancel(sigma(expr))))
    expr2 = numer(cancel(sigma(expr)))
    s_bc, s_ca, s_ab = (b - c) ** 2, (c - a) ** 2, (a - b) ** 2
    fnum = dict1(expr0).__len__()
    varlistf = sympy.symbols('v:{}:a'.format(fnum))
    s_a, s_b, s_c = 0, 0, 0
    for i in range(0, fnum):
        s_a += varlistf[i] * dict1(expr0)[i]
        s_b += varlistf[i] * sympy.simplify(ex_0('{0}'.format(dict1(expr0)[i])))
        s_c += varlistf[i] * sympy.simplify(ex_1('{0}'.format(dict1(expr0)[i])))
    ineq = s_a * s_bc + s_b * s_ca + s_c * s_ab
    ineq0 = expand(s_a * s_bc + s_b * s_ca + s_c * s_ab)
    func0 = sympy.poly(ineq0 - expr2, a, b, c)
    equlist0 = []
    for i in range(0, dict0(expr0).__len__()):
        equlist0.append(func0.coeff_monomial(dict0(expr0)[i]))
    ans = solve(equlist0, varlistf)
    result0 = ineq.subs(ans)
    result2_a, result2_b, result2_c = s_a.subs(ans), s_b.subs(ans), s_c.subs(ans)
    result0 = str(result0)
    varlistf0 = [str(varlistf[i]) for i in range(0, fnum)]
    varlistf1, i = [], 0
    result2 = s_a.subs(ans)
    print('[通式] ', 'Σ (', result2, ') * ( b - c ) ** 2')
    for j in range(0, fnum):
        if varlistf0[j] in result0:
            varlistf1.append(varlistf0[j])
    fnum0 = varlistf1.__len__()
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
        print('[默认] ', 'Σ (', result2, ') * ( b - c ) ** 2')
    if judge1(expr0) >= 5:
        add_a = sympy.poly(result2_a, a, b, c)
        add0_5 = {varlistf2[i]: 1 for i in range(0, fnum0)}
        result2 = numer(factor(add_a.subs(add0_5)))
        print('[默认] ', 'Σ (', result2, ') * ( b - c ) ** 2')


def zero(deg0):
    s_bc, s_ca, s_ab = (b - c) ** 2, (c - a) ** 2, (a - b) ** 2
    if deg0 >= 3:
        expr0 = str(a ** int(deg0))
    dictnew = dict1(expr0)
    fnum = dict1(expr0).__len__()
    varlistf = sympy.symbols('v:{}:a'.format(fnum))
    s_a, s_b, s_c = 0, 0, 0
    for i in range(0, fnum):
        s_a += varlistf[i] * dict1(expr0)[i]
        s_b += varlistf[i] * sympy.simplify(ex_0('{0}'.format(dict1(expr0)[i])))
        s_c += varlistf[i] * sympy.simplify(ex_1('{0}'.format(dict1(expr0)[i])))
    eq, eq1 = s_a * s_bc + s_b * s_ca + s_c * s_ab, 0
    eq0 = expand(s_a * s_bc + s_b * s_ca + s_c * s_ab)
    func0 = sympy.poly(eq0, a, b, c)
    equlist0 = []
    for i in range(0, dict0(expr0).__len__()):
        equlist0.append(func0.coeff_monomial(dict0(expr0)[i]))
    ans = solve(equlist0, varlistf)
    result0 = eq.subs(ans)
    result2_a, result2_b, result2_c = s_a.subs(ans), s_b.subs(ans), s_c.subs(ans)
    result0 = str(result0)
    varlistf0 = [str(varlistf[i]) for i in range(0, fnum)]
    varlistf1, i = [], 0
    result2 = s_a.subs(ans)
    print(equlist0)
    print('[通式] ', 'Σ (', result2, ') * ( b - c ) ** 2')
    for j in range(0, fnum):
        if varlistf0[j] in result0:
            varlistf1.append(varlistf0[j])
    fnum0 = varlistf1.__len__()
    varlistf2 = [[] for i in range(0, fnum0)]
    for k in range(0, fnum0):
        varlistf2[k] = sympy.symbols(varlistf1[k])
    print('[参数] ', varlistf2)
    add_a = sympy.poly(result2_a, a, b, c)
    add0_5 = {varlistf2[i]: 1 for i in range(0, fnum0)}
    result2 = numer(factor(add_a.subs(add0_5)))
    print('[默认] ', 'Σ (', result2, ') * ( b - c ) ** 2')


def sc1_5(expr):
    print('[整理] ', normal0(expr))
    expr0 = str(numer(cancel(sigma(expr))))
    expr2 = numer(cancel(sigma(expr)))
    s_bc, s_ca, s_ab = (a - b) * (a - c), (b - c) * (b - a), (c - a) * (c - b)
    fnum = dict1(expr0).__len__()
    varlistf = sympy.symbols('v:{}:a'.format(fnum))
    s_a, s_b, s_c = 0, 0, 0
    for i in range(0, fnum):
        s_a += varlistf[i] * dict1(expr0)[i]
        s_b += varlistf[i] * sympy.simplify(ex_0('{0}'.format(dict1(expr0)[i])))
        s_c += varlistf[i] * sympy.simplify(ex_1('{0}'.format(dict1(expr0)[i])))
    ineq = s_a * s_bc + s_b * s_ca + s_c * s_ab
    ineq0 = expand(s_a * s_bc + s_b * s_ca + s_c * s_ab)
    func0 = sympy.poly(ineq0 - expr2, a, b, c)
    equlist0 = []
    for i in range(0, dict0(expr0).__len__()):
        equlist0.append(func0.coeff_monomial(dict0(expr0)[i]))
    ans = solve(equlist0, varlistf)
    result0 = ineq.subs(ans)
    result2_a, result2_b, result2_c = s_a.subs(ans), s_b.subs(ans), s_c.subs(ans)
    result0 = str(result0)
    varlistf0 = [str(varlistf[i]) for i in range(0, fnum)]
    varlistf1, i = [], 0
    result2 = s_a.subs(ans)
    print('[通式] ', 'Σ (', result2, ') * ( a - b ) * ( a - c )')
    for j in range(0, fnum):
        if varlistf0[j] in result0:
            varlistf1.append(varlistf0[j])
    fnum0 = varlistf1.__len__()
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
        print('[默认] ', 'Σ (', result2, ') * ( a - b ) * ( a - c )')
    if judge1(expr0) >= 5:
        add_a = sympy.poly(result2_a, a, b, c)
        add0_5 = {varlistf2[i]: 1 for i in range(0, fnum0)}
        result2 = numer(factor(add_a.subs(add0_5)))
        print('[默认] ', 'Σ (', result2, ') * ( a - b ) * ( a - c )')


def dict0(expr):
    termlist0 = []
    jud0 = judge1(expr)
    for i in range(0, jud0 + 1):
        for j in range(0, jud0 + 1):
            for k in range(0, jud0 + 1):
                if i + j + k == jud0:
                    termlist0.append(a ** i * b ** j * c ** k)
    return termlist0


def dict1(expr):
    termlist1 = []
    jud1 = judge1(expr)
    for i in range(0, jud1 - 1):
        for j in range(0, jud1 - 1):
            for k in range(0, jud1 - 1):
                if i + j + k == jud1 - 2:
                    termlist1.append(a ** i * b ** j * c ** k)
    return termlist1


def info():
    print(' 三元轮换对称不等式运算程序 for Python 3\n')
    print(' ----------------- Contact -----------------')
    print(' *cx2020 Jinan, Shandong')
    print(' 2913026224@qq.com\n')
    print(' ------------- Current Version -------------')
    print(' ver 1.6 [20201229] Jinan, Shandong')
    print(' 该版本包含的核心算法版本是 仅 ver 1.5')
    print(' 该版本仅支持齐次不等式\n')
    print(' ------------- History Version -------------')
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
    print(' [功能二] cs1_5(expr)')
    print('  [说明一] 对三元齐次轮换对称不等式作SOS分拆；')
    print('  [说明二] 对三元轮换对称不等式作SOS分拆得到通式后，再输出一个易于展示的形式；')
    print('  [注意一] expr的类型是字符串，因此需要添加英文引号；')
    print('  [注意二] 本函数会首先对表达式求和，即对表达式加上 Σ（轮换和）符号，通分后提取分子部分；')
    print('  [注意三] 有多种SOS分拆结果时，会将通式参数化表示（v[i]a）.\n')
    print(' [功能三] sc1_5(expr)')
    print('  [说明一] 对三元齐次轮换对称不等式作Schur分拆；')
    print('  [说明二] 对三元轮换对称不等式作Schur分拆得到通式后，再输出一个易于展示的形式；')
    print('  [注意一] expr的类型是字符串，因此需要添加英文引号；')
    print('  [注意二] 本函数会首先对表达式求和，即对表达式加上 Σ（轮换和）符号，通分后提取分子部分；')
    print('  [注意三] 有多种Schur分拆结果时，会将通式参数化表示（v[i]a）.\n')
    print(' [功能四] ast1_5(expr)')
    print('  [说明一] 对三元齐次轮换对称不等式通分，并对整理后的分子作差分代换；')
    print('  [说明二] 令 (a, b, c) ➡ (a, a + s, a + t)；')
    print('  [注意一] expr的类型是字符串，因此需要添加英文引号；')
    print('  [注意二] 本函数会首先对表达式求和，即对表达式加上 Σ（轮换和）符号，通分后提取分子部分.\n')
