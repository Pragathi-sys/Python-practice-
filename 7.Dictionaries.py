color={
    "c1":"red",
    "c2":"black",
    "c3":"white"
}
print(color["c2"])
print(color.get("c4","not found"))
color["c4"]="white"
color["c3"]="pink"
color.pop("c2")
del color["c3"]
color.clear( 3)
print(color)