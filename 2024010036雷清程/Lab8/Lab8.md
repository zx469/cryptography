# 密码学 习题集 - 认证加密与高级加密构造
---
## 第 1 题
攻击者截获了如下密文（十六进制编码）：
```text
20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d
```
攻击者知道明文是字符串 `"Pay Bob 100$"` 的 ASCII 编码（不包含引号）。攻击者还知道所使用的加密方式是以 AES 为底层分组密码、带随机 IV 的 CBC 加密。
请说明攻击者可以如何修改密文，使其解密后变为 `"Pay Bob 500$"`。修改后的密文是什么（十六进制编码）？这说明 CBC 加密本身不提供完整性保护。
修改后的密文：
```text
20814804c1767293bd9f1d9cab3bc3e7ac1e37bfb15599e5f40eef805488281d
```
---
## 第 2 题
设 $(E, D)$ 是一个加密系统，密钥空间为 $K$，消息空间为 $\{0,1\}^n$，密文空间为 $\{0,1\}^s$。假设 $(E, D)$ 提供认证加密。以下哪些系统也提供认证加密？（$\|$ 表示字符串拼接，可能有多个正确答案）
- [x] $E'(k, m) = (E(k, m), 0)$，且
  $$
  D'(k, (c, b)) =
  \begin{cases}
  D(k, c) & \text{若 } b = 0 \\
  \bot & \text{否则}
  \end{cases}
  $$
- [ ] $E'(k, m) = (E(k, m), 0)$，且
  $$
  D'(k, (c, b)) = D(k, c)
  $$
- [x] $E'(k, m) = E(k, m) \oplus 1^s$，且
  $$
  D'(k, c) = D(k, c \oplus 1^s)
  $$
- [ ] $E'(k, m) = (E(k, m), E(k, m))$，且
  $$
  D'(k, (c_1, c_2)) =
  \begin{cases}
  D(k, c_1) & \text{若 } D(k, c_1) = D(k, c_2) \\
  \bot & \text{否则}
  \end{cases}
  $$
---
## 第 3 题
如果需要构建一个应用，并且该应用需要在同一个密钥下加密多条消息，应该使用哪种加密方式？（暂时忽略密钥生成和密钥管理问题）
- [ ] 自行实现 MAC-then-Encrypt
- [ ] 使用标准实现的随机化计数器模式
- [ ] 使用标准实现的带随机 IV 的 CBC 加密
- [x] 使用标准实现的认证加密模式之一，例如 GCM、CCM、EAX 或 OCB
---
## 第 4 题
设 $(E, D)$ 是一个对称加密系统，消息空间为 $M$（可以认为 $M$ 只包含较短消息，例如 32 字节消息）。对 $M$ 中的消息定义如下 MAC 系统 $(S, V)$：
$$
S(k, m) := E(k, m)
$$
$$
V(k, m, t) :=
\begin{cases}
1 & \text{若 } D(k, t) = m \\
0 & \text{否则}
\end{cases}
$$
为了使该 MAC 系统安全，加密系统 $(E, D)$ 需要满足什么性质？
- [x] 认证加密
- [ ] 确定性选择明文攻击下的语义安全
- [ ] 完美保密性
- [ ] 语义安全
---
## 第 5 题
课上，我们讨论了如何从共享秘密派生会话密钥。问题在于，当共享秘密不是均匀分布时应该如何处理。本题说明：如果直接把非均匀秘密当作 PRF 的密钥，可能会得到非均匀的输出。因此，会话密钥不能直接通过把非均匀秘密作为 PRF 密钥来派生，而应该使用 HKDF 之类的密钥派生函数。
假设 $k$ 是从密钥空间 $\{0,1\}^{256}$ 中采样得到的非均匀秘密密钥。具体而言，$k$ 从所有最高有效 128 位全为 0 的密钥集合中均匀采样。换句话说，$k$ 是从密钥空间的一个较小子集中均匀选取的。更精确地说，对于所有 $c \in \{0,1\}^{256}$：
$$
\Pr[k = c] =
\begin{cases}
1 / 2^{128} & \text{若 } \operatorname{MSB}_{128}(c) = 0^{128} \\
0 & \text{否则}
\end{cases}
$$
设 $F(k, x)$ 是一个输入空间为 $\{0,1\}^{256}$ 的安全 PRF。以下哪个构造在密钥 $k$ 从完整密钥空间 $\{0,1\}^{256}$ 均匀采样时是安全 PRF，但在密钥从上述非均匀分布采样时是不安全的？
- [x] 
  $$
  F'(k, x) =
  \begin{cases}
  F(k, x) & \text{若 } \operatorname{MSB}_{128}(k) = 0^{128} \\
  1^{256} & \text{否则}
  \end{cases}
  $$
- [x] 
  $$
  F'(k, x) =
  \begin{cases}
  F(k, x) & \text{若 } \operatorname{MSB}_{128}(k) \neq 0^{128} \\
  1^{256} & \text{否则}
  \end{cases}
  $$
- [ ] $F'(k, x) = F(k, x)$
- [x] 
  $$
  F'(k, x) =
  \begin{cases}
  F(k, x) & \text{若 } \operatorname{MSB}_{128}(k) \neq 1^{128} \\
  0^{256} & \text{否则}
  \end{cases}
  $$
---
## 第 6 题
在什么场景下可以使用像 SIV 这样的确定性认证加密（DAE）？
- [ ] 在同一个密钥下反复加密同一条固定消息
- [ ] 在语音通话中使用同一个密钥分别加密许多数据包
- [x] 消息从足够大的空间中随机选取，因此消息不太可能重复
- [ ] 在同一个密钥下加密数据库中的多条记录，并且相同记录可能重复多次
---
## 第 7 题
设 $E(k, x)$ 是一个安全分组密码。考虑如下可调分组密码：
$$
E'((k_1, k_2), t, x) = E(k_1, x) \oplus E(k_2, t)
$$
这个可调分组密码是否安全？
- [ ] 不安全，因为对于 $t \neq t'$，有
  $$
  E'((k_1,k_2),t,0) \oplus E'((k_1,k_2),t',1)
  =
  E'((k_1,k_2),t',1) \oplus E'((k_1,k_2),t',0)
  $$
- [x] 不安全，因为对于 $x \neq x'$ 且 $t \neq t'$，有
  $$
  E'((k_1,k_2),t,x) \oplus E'((k_1,k_2),t',x)
  =
  E'((k_1,k_2),t,x') \oplus E'((k_1,k_2),t',x')
  $$
- [ ] 不安全，因为对于 $x \neq x'$，有
  $$
  E'((k_1,k_2),0,x) \oplus E'((k_1,k_2),1,x)
  =
  E'((k_1,k_2),0,x') \oplus E'((k_1,k_2),1,x')
  $$
- [ ] 不安全，因为对于 $x \neq x'$，有
  $$
  E'((k_1,k_2),0,x) \oplus E'((k_1,k_2),0,x)
  =
  E'((k_1,k_2),0,x') \oplus E'((k_1,k_2),0,x')
  $$
- [ ] 是安全的，前提是 $E$ 是安全分组密码
---
## 第 8 题
课上我们讨论了保留格式加密。保留格式加密是在某个预先指定的定义域 $\{0,\ldots,s-1\}$ 上的 PRP。回顾课程中给出的构造，它分为两步，其中第二步通过不断迭代 PRP，直到输出落入集合 $\{0,\ldots,s-1\}$。
假设我们尝试只使用第二步，由 AES 构造一个保留格式的信用卡加密系统。也就是说，我们从定义域为 $\{0,1\}^{128}$ 的 PRP 出发，希望构造一个定义域为 $10^{16}$ 的 PRP。如果只使用步骤 2，那么对于定义域为 $10^{16}$ 的 PRP，每次求值期望需要多少次 AES 迭代？
- [x] $2^{128} / 10^{16} \approx 3.4 \times 10^{22}$
- [ ] $2^{16}$
- [ ] $10^{16}$
- [ ] $10^{16} / 2^{128}$
---
## 第 9 题
设 $(E, D)$ 是一个安全的可调分组密码。定义如下 MAC 系统 $(S, V)$：
$$
S(k, m) := E(k, m, 0)
$$
$$
V(k, m, \text{tag}) :=
\begin{cases}
1 & \text{若 } E(k, m, 0) = \text{tag} \\
0 & \text{否则}
\end{cases}
$$
也就是说，消息 $m$ 被用作 tweak，而传给 $E$ 的明文始终设为 $0$。这个 MAC 安全吗？
- [ ] 这取决于具体的可调分组密码
- [x] `安全`
- [ ] 不安全
---
## 第 10 题
课上我们讨论了填充预言机攻击。这类选择密文攻击可以攻破实现不当的 MAC-then-Encrypt 系统。考虑一个实现了 MAC-then-Encrypt 的系统，其中加密使用以 AES 为底层分组密码、带随机 IV 的 CBC 模式。
假设该系统容易受到填充预言机攻击。攻击者截获了一段 64 字节密文 $c$，其中前 16 字节是 IV，剩余 48 字节是加密载荷。为了在最坏情况下解密完整的 48 字节载荷，攻击者需要多少次选择密文查询？回顾：填充预言机攻击一次解密一个字节。
- [x] 12288
- [ ] 1024
- [ ] 12240
- [ ] 256
---
## 第 11 题
在使用 tweak 之前是否需要对其进行加密？也就是说，以下是否是一个安全的可调 PRP？
设 $E_{PRP}$ 是一个安全的分组密码，$P(t, i)$ 是一个公开函数（例如 $P(t, i) = E_{PRP}(t, i)$）。考虑如下可调分组密码构造：
$$
E'\big(k, (t, i), x\big) = E_{PRP}\big(k, x \oplus P(t, i)\big) \oplus P(t, i)
$$
其中 $t$ 是 tweak，$i$ 是分组索引，$x$ 是明文。
- [ ] 是的，它是安全的
- [ ] 不安全：$E(k, (t,1), P(t,2)) \oplus E(k, (t,2), P(t,1)) = P(t,1)$
- [x] 不安全：$E(k, (t,1), P(t,1)) \oplus E(k, (t,2), P(t,2)) = P(t,1) \oplus P(t,2)$
- [ ] 不安全：$E(k, (t,1), P(t,1)) \oplus E(k, (t,2), P(t,2)) = 0$
---
## 第 12 题
使用固定 IV 的计数器模式是否是 CPA 安全的？
考虑一个 CTR 模式加密，其中计数器模式的初始值（IV）是固定的（FIV），而不是每次加密随机选择。加密公式为：
$$
c = m \oplus F(k, \text{FIV}) \parallel F(k, \text{FIV}+1) \parallel \ldots \parallel F(k, \text{FIV}+L)
$$
- [ ] 是（Yes）
- [x] 否（No）
- [ ] 视情况而定（It depends）
---
## 第 13 题
在密钥派生函数（KDF）中，CTX（上下文参数）的目的是什么？
考虑如下 KDF 构造：
$$
\text{KDF}(SK, CTX, L) := F(SK, (CTX \parallel 0)) \parallel F(SK, (CTX \parallel 1)) \parallel \ldots \parallel F(SK, (CTX \parallel L))
$$
其中 $SK$ 是主密钥，$CTX$ 是上下文字符串，$L$ 是派生密钥长度。
- [x] 即使两个应用采样相同的 $SK$，它们也会获得独立的密钥
- [ ] 给字符串标注应用程序名称是良好的做法
- [ ] 这没有意义
---
## 第 14 题
SSH 协议面临一个安全攻击，该攻击利用了以下两个问题：
1. 非原子解密（non-atomic decrypt）
2. 长度字段（len field）在认证之前就被解密和使用
你会如何重新设计 SSH 以抵抗这种攻击？
- [ ] 发送未加密但经过 MAC 认证的长度字段（Send the length field unencrypted (but MAC-ed)）
- [ ] 用 encrypt-then-MAC 替换 encrypt-and-MAC（Replace encrypt-and-MAC by encrypt-then-MAC）
- [x] 在长度字段后立即添加对 (seq-num, length) 的 MAC（Add a MAC of (seq-num, length) right after the len field）
- [ ] 移除长度字段，通过每次接收一个字节后验证 MAC 来识别数据包边界（Remove the length field and identify packet boundary by verifying the MAC after every received byte）
---
## 第 15 题
如果 TLS 使用计数器模式（CTR）而不是 CBC 模式，填充预言机攻击（padding oracle attack）是否仍然有效？（即使用 MAC-then-CTR 构造）
- [ ] 是的，填充预言机影响所有加密方案（Yes, padding oracles affect all encryption schemes）
- [ ] 取决于使用哪种分组密码（It depends on what block cipher is used）
- [x] 不，计数器模式不需要使用填充（No, counter mode need not use padding）
---
## 第 16 题
考虑一个使用 CBC 模式加密的系统，其中使用随机 IV。攻击者截获了一个数据包，其明文结构为 `dest = 80 | data`（目标端口为 80）。攻击者希望修改密文，使得解密后的明文变为 `dest = 25 | data`（目标端口改为 25），而不需要知道加密密钥。
在 CBC 模式中，第一块明文的解密公式为：
$$
m[0] = D(k, c[0]) \oplus IV = \text{``dest=80...''}
$$
攻击者应该将 IV 修改为什么值 $IV'$，才能使得解密后的第一块明文变为 `dest = 25`？
- [ ] $IV' = IV \oplus (\ldots 25 \ldots)$
- [ ] $IV' = IV \oplus (\ldots 80 \ldots)$
- [x] $IV' = IV \oplus (\ldots 80 \ldots) \oplus (\ldots 25 \ldots)$
- [ ] 无法实现（It can't be done）
---