import sympy
from sympy import *

print('ver 1.2 [20201221]')
print('*cx2020 Jinan, Shandong')

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


def ast(expr):
    expr0 = [i for i in expr]
    exprast = ''
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
        exprast += expr0[i]
    exprast = str(exprast)
    return exprast


def auto0(expr):
    expr0 = ast(str(numer(cancel(sigma(expr)))))
    return expr0


def final0(expr):
    expr0 = sympy.simplify(auto0(expr))
    expr1 = expand(expr0)
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


def final1(expr):
    form = judge0(expr)
    expr = final0(expr)
    if form == 0:
        expr1 = collect(expr, 'a')
        return expr1
    if form == 1:
        expr1 = collect(expr, 'x')
        return expr1


def final2(expr):
    expr = str(final1(expr))
    expr1 = expr.split('**')
    len0 = expr1.__len__()
    expr2 = ''
    for i in range(0, len0 - 1):
        expr2 += expr1[i] + '^'
    expr2 = str(expr2 + expr1[len0 - 1])
    return expr2


def final3(expr):
    expr = str(cs1_1(expr))
    expr1 = expr.split('**')
    len0 = expr1.__len__()
    expr2 = ''
    for i in range(0, len0 - 1):
        expr2 += expr1[i] + '^'
    expr2 = str(expr2 + expr1[len0 - 1])
    return expr2


def normal0(expr):
    expr0 = sympy.simplify(numer(cancel(sigma(expr))))
    return expr0


def cs1_1(expr):
    expr0 = normal0(expr)
    s_bc = (b - c) ** 2
    s_ca = (c - a) ** 2
    s_ab = (a - b) ** 2
    s_a = d * a + a12 * b + a13 * c
    s_b = a21 * a + d * b + a23 * c
    s_c = a31 * a + a32 * b + d * c
    ineq = s_a * s_bc + s_b * s_ca + s_c * s_ab
    ineq0 = expand(s_a * s_bc + s_b * s_ca + s_c * s_ab)
    func0 = sympy.poly(ineq0 - expr0, a, b, c)
    equ1, equ2, equ3 = func0.coeff_monomial(a ** 3), func0.coeff_monomial(a ** 2 * b), func0.coeff_monomial(a * b ** 2)
    equ4, equ5, equ6 = func0.coeff_monomial(b ** 3), func0.coeff_monomial(b ** 2 * c), func0.coeff_monomial(b * c ** 2)
    equ7, equ8, equ9 = func0.coeff_monomial(c ** 3), func0.coeff_monomial(c ** 2 * a), func0.coeff_monomial(c * a ** 2)
    equ10 = func0.coeff_monomial(a * b * c)
    ans = solve([equ1, equ2, equ3, equ4, equ5, equ6, equ7, equ8, equ9, equ10], [d, a12, a13, a21, a23, a31, a32])
    result = ineq.subs(ans)
    return result


def cs1_2(expr):
    expr0 = str(numer(cancel(sigma(expr))))
    expr2 = numer(cancel(sigma(expr)))
    s_bc = (b - c) ** 2
    s_ca = (c - a) ** 2
    s_ab = (a - b) ** 2
    fnum = dict1(expr0).__len__()
    varlista = sympy.symbols('avar:{}'.format(fnum))
    varlistb = sympy.symbols('bvar:{}'.format(fnum))
    varlistc = sympy.symbols('cvar:{}'.format(fnum))
    s_a, s_b, s_c = 0, 0, 0
    for i in range(0, fnum):
        s_a += varlista[i]*dict1(expr0)[i]
    for i in range(0, fnum):
        s_b += varlistb[i]*dict1(expr0)[i]
    for i in range(0, fnum):
        s_c += varlistc[i]*dict1(expr0)[i]
    ineq = s_a * s_bc + s_b * s_ca + s_c * s_ab
    ineq0 = expand(s_a * s_bc + s_b * s_ca + s_c * s_ab)
    func0 = sympy.poly(ineq0 - expr2, a, b, c)
    equlist0 = []
    for i in range(0, dict0(expr0).__len__()):
        equlist0.append(func0.coeff_monomial(dict0(expr0)[i]))
    ans = solve(equlist0, varlista + varlistb + varlistc)
    result = ineq.subs(ans)
    print(s_a, s_b, s_c)
    return result


def dict0(expr):
    termlist0 = []
    for i in range(0, judge1(expr) + 1):
        for j in range(0, judge1(expr) + 1):
            for k in range(0, judge1(expr) + 1):
                if i + j + k == judge1(expr):
                    termlist0.append(a ** i * b ** j * c ** k)
    return termlist0


def dict1(expr):
    termlist1 = []
    for i in range(0, judge1(expr) - 1):
        for j in range(0, judge1(expr) - 1):
            for k in range(0, judge1(expr) - 1):
                if i + j + k == judge1(expr) - 2:
                    termlist1.append(a ** i * b ** j * c ** k)
    return termlist1
