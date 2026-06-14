
---

## 第 1 题

考虑课上讨论的使用在线可信第三方（TTP）的玩具密钥交换协议。假设 Alice、Bob 和 Carol 是该系统中的三个用户（系统中还有许多其他用户），他们分别与 TTP 共享秘密密钥 $k_a$、$k_b$、$k_c$。

他们希望生成一个群组会话密钥 $k_{ABC}$，该密钥应当被 Alice、Bob 和 Carol 知道，但不能被窃听者知道。应如何修改课上的协议，使其支持这种群组密钥交换？（注意：这些协议都不能抵抗主动攻击。）

- [ ] Alice 联系 TTP。TTP 生成随机的 $k_{ABC}$，并发送给 Alice：

  $$
  E(k_a, k_{ABC}),\quad
  \text{ticket}_1 \leftarrow E(k_c, E(k_b, k_{ABC})),\quad
  \text{ticket}_2 \leftarrow E(k_b, E(k_c, k_{ABC}))
  $$

  Alice 将 $k_{ABC}$ 发送给 Bob，并将 $k_{ABC}$ 发送给 Carol。

- [ ] Bob 联系 TTP。TTP 生成随机的 $k_{AB}$ 和随机的 $k_{BC}$，并发送给 Bob：

  $$
  E(k_a, k_{AB}),\quad
  \text{ticket}_1 \leftarrow E(k_a, k_{AB}),\quad
  \text{ticket}_2 \leftarrow E(k_c, k_{BC})
  $$

  Bob 将 $\text{ticket}_1$ 发送给 Alice，将 $\text{ticket}_2$ 发送给 Carol。

- [x] Alice 联系 TTP。TTP 生成随机的 $k_{ABC}$，并发送给 Alice：

  $$
  E(k_a, k_{ABC}),\quad
  \text{ticket}_1 \leftarrow E(k_b, k_{ABC}),\quad
  \text{ticket}_2 \leftarrow E(k_c, k_{ABC})
  $$

  Alice 将 $\text{ticket}_1$ 发送给 Bob，将 $\text{ticket}_2$ 发送给 Carol。

---

## 第 2 题

设 $G$ 是一个有限循环群（例如 $G = \mathbb{Z}_p^*$），生成元为 $g$。假设 Diffie-Hellman 函数

$$
\operatorname{DH}_g(g^x, g^y) = g^{xy}
$$

在 $G$ 中难以计算。以下哪些函数也难以计算？

像往常一样，请找出下面的函数 $f$，使得如下逆否命题成立：如果 $f(\cdot,\cdot)$ 容易计算，那么 $\operatorname{DH}_g(\cdot,\cdot)$ 也容易计算。若能证明这一点，则可推出：如果 $\operatorname{DH}_g$ 在 $G$ 中是困难的，那么 $f$ 也必须是困难的。

- [x] $f(g^x, g^y) = g^{x(y+1)}$

- [x] $f(g^x, g^y) = (g^{3xy}, g^{2xy})$（该函数输出 $G$ 中的一对元素）

- [ ] $f(g^x, g^y) = g^{x-y}$

---

## 第 3 题

假设我们对 Diffie-Hellman 协议做如下修改：Alice 像通常一样，随机选择 $a \in \{1,\ldots,p-1\}$，并向 Bob 发送

$$
A \leftarrow g^a
$$

但 Bob 随机选择 $b \in \{1,\ldots,p-1\}$，并向 Alice 发送

$$
B \leftarrow g^{1/b}
$$

他们可以生成什么共享秘密？应如何生成？

- [ ] 共享秘密为 $g^{a/b}$。Alice 计算 $B^{1/b}$，Bob 计算 $A^a$。

- [ ] 共享秘密为 $g^{ab}$。Alice 计算 $B^{1/a}$，Bob 计算 $A^b$。

- [x] 共享秘密为 $g^{a/b}$。Alice 计算 $B^a$，Bob 计算 $A^{1/b}$。

- [ ] 共享秘密为 $g^{ab}$。Alice 计算 $B^a$，Bob 计算 $A^b$。

---

## 第 4 题

考虑课上的使用公钥加密的玩具密钥交换协议。

假设 Bob 向 Alice 发送回复 $c \leftarrow E(pk, x)$ 时，还在密文后附加一个 MAC 标签

$$
t := S(x, c)
$$

因此 Alice 收到的是二元组 $(c,t)$。Alice 验证标签 $t$，若标签验证失败，则拒绝 Bob 的消息。

这个额外步骤是否能阻止课上描述的中间人攻击？

- [ ] 取决于使用的 MAC 系统
- [ ] 能
- [x] 不能
- [ ] 取决于使用的公钥加密系统

---

## 第 5 题

7 和 23 互素，因此一定存在整数 $a$ 和 $b$，使得

$$
7a + 23b = 1
$$

请找出满足条件且 $a > 0$ 尽可能小的一组整数 $(a,b)$。

给定这组 $(a,b)$ 后，能否确定 $7$ 在 $\mathbb{Z}_{23}$ 中的逆元？

请按逗号分隔的格式填写 $a$、$b$，以及 $7^{-1}$ 在 $\mathbb{Z}_{23}$ 中的值。

答案：

```text
10,-3,10
```

---

## 第 6 题

求解 $\mathbb{Z}_{19}$ 中的方程：

$$
3x + 2 = 7
$$

答案：

```text
8
```

---

## 第 7 题

$\mathbb{Z}_{35}^*$ 中有多少个元素？

答案：

```text
24
```

---

## 第 8 题

不使用计算器，求：

$$
2^{10001} \bmod 11
$$

提示：使用费马小定理。

答案：

```text
2
```

---

## 第 9 题

继续上一题，求：

$$
2^{245} \bmod 35
$$

提示：使用欧拉定理，你不需要计算器。

答案：

```text
32
```

---

## 第 10 题

2 在 $\mathbb{Z}_{35}^*$ 中的阶是多少？

答案：

```text
12
```

---

## 第 11 题

以下哪些数是 $\mathbb{Z}_{13}^*$ 的生成元？

- [ ] $4,\quad \langle 4 \rangle = \{1,4,3,12,9,10\}$

- [x] $6,\quad \langle 6 \rangle = \{1,6,10,8,9,2,12,7,3,5,4,11\}$

- [ ] $3,\quad \langle 3 \rangle = \{1,3,9\}$

- [x] $7,\quad \langle 7 \rangle = \{1,7,10,5,9,11,12,6,3,8,4,2\}$

- [ ] $8,\quad \langle 8 \rangle = \{1,8,12,5\}$

---

## 第 12 题

求解 $\mathbb{Z}_{23}$ 中的方程：

$$
x^2 + 4x + 1 = 0
$$

请使用二次公式方法。

答案：

```text
5,14
```

---

## 第 13 题

求 2 在 $\mathbb{Z}_{19}$ 中的 11 次根，即求：

$$
2^{1/11} \in \mathbb{Z}_{19}
$$

提示：注意 $11^{-1} = 5$ 在 $\mathbb{Z}_{18}$ 中成立。

答案：

```text
13
```

---

## 第 14 题

求 $\mathbb{Z}_{13}$ 中以 2 为底、5 的离散对数：

$$
\operatorname{Dlog}_2(5)
$$

回忆：2 在 $\mathbb{Z}_{13}$ 中的幂为

$$
\langle 2 \rangle = \{1,2,4,8,3,6,12,11,9,5,10,7\}
$$

答案：

```text
9
```

---

## 第 15 题

如果 $p$ 是素数，那么 $\mathbb{Z}_p^*$ 中有多少个生成元？

- [ ] $(p+1)/2$
- [ ] $\varphi(p)$
- [x] $\varphi(p-1)$
- [ ] $\sqrt{p}$

---


