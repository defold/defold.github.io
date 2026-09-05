# extension-spine

**Namespace:** `resource`
**Language:** Lua
**Type:** Extension

Functions for creating Spine resources dynamically

## API

### resource.create_spinescene
*Type:* FUNCTION
Creates a spinescene resource (.spinescenec) from runtime data. Creates a Spine scene resource dynamically at runtime. This allows loading Spine animations from data rather than pre-built assets. The atlas path must reference a compiled `.texturesetc` resource. The created spinescene is tracked for cleanup when the collection unloads; internal intermediate JSON is removed automatically.

**Parameters**

- `path` (string) - The target resource path. Must end with .spinescenec
- `options` (table) - Table with fields
  - `spine_data` (string) - JSON bytes of the Spine skeleton
  - `atlas_path` (string) - Path to the compiled atlas resource (.texturesetc)

**Examples**

`
`
`
l
u
a

f
u
n
c
t
i
o
n

i
n
i
t
(
s
e
l
f
)

-
-

L
o
a
d

S
p
i
n
e

J
S
O
N

d
a
t
a

l
o
c
a
l

j
s
o
n

=

s
y
s
.
l
o
a
d
_
r
e
s
o
u
r
c
e
(
"
/
d
a
t
a
/
c
h
a
r
a
c
t
e
r
.
s
p
i
n
e
j
s
o
n
"
)

-
-

C
r
e
a
t
e

s
p
i
n
e
s
c
e
n
e

d
y
n
a
m
i
c
a
l
l
y

l
o
c
a
l

s
c
e
n
e

=

r
e
s
o
u
r
c
e
.
c
r
e
a
t
e
_
s
p
i
n
e
s
c
e
n
e
(
"
/
d
y
n
/
c
h
a
r
a
c
t
e
r
.
s
p
i
n
e
s
c
e
n
e
c
"
,

{

s
p
i
n
e
_
d
a
t
a

=

j
s
o
n
,

a
t
l
a
s
_
p
a
t
h

=

"
/
t
e
x
t
u
r
e
s
/
c
h
a
r
a
c
t
e
r
.
a
.
t
e
x
t
u
r
e
s
e
t
c
"

}
)

g
o
.
s
e
t
(
"
/
g
u
i

s
w
a
p
"
,

"
s
p
i
n
e
_
s
c
e
n
e
"
,

s
c
e
n
e
,

{

k
e
y

=

"
s
p
i
n
e
b
o
y
"

}
)

-
-

I
t
'
s

p
o
s
i
s
b
l
e

t
o

s
e
t

f
r
o
m

g
u
i

c
o
m
p
o
n
e
n
t

i
t
s
e
l
f

a
s

w
e
l
l
:

-
-

g
u
i
.
s
e
t
(
m
s
g
.
u
r
l
(
)
,

"
s
p
i
n
e
_
s
c
e
n
e
"
,

s
c
e
n
e
,

{

k
e
y

=

"
s
p
i
n
e
b
o
y
"

}
)

e
n
d

`
`
`
