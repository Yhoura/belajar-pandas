# %%
s = pd.Series([10,20,30], index=["a","b","c"])
s


# %%
f = pd.Series([1,2,3,4])
f
# %%
data = {
    "nama":["wiyono","rizki","dewantoro"],
    "umur":[12,22,23],
    "email":["wiyono@gmail.com","rizki@gmail.com","dewantoro@gmail.com"]
}
j = pd.DataFrame(data)
j[["nama"],["email"]]

# %%
