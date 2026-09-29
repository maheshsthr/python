import module_emp as emp

basic = 35000
gross =basic+  emp.da(basic) + emp.hra(basic)
net = gross - emp.pf(basic) - emp.itax(basic)
print(f"Basic {basic}\nGross : {gross}\nNet {net}")