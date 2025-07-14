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
j = pd.DataFrame(data).set_index("email")
j["nama"]
# %%
l = pd.DataFrame(data)
l['email']
# %%
i= pd.DataFrame(data)
i.loc[0]

# %%
j.loc["wiyono@gmail.com"]
# %%
j.iloc[1]
# %%
