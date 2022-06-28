def findtotalevent(df1_row):
  total_views = df2[(df2["contentId"]==df1_row["contentId"]) & df2["eventType"]=="VIEW"].shape[0]
  total_like = df2[(df2["contentId"]==df1_row["contentId"]) & df2["eventType"]=="LIKE"].shape[0]
  total_bookmark = df2[(df2["contentId"]==df1_row["contentId"]) & df2["eventType"]=="BOOKMARK"].shape[0]
  total_commentcreated = df2[(df2["contentId"]==df1_row["contentId"]) & df2["eventType"]=="COMMENT CREATED"].shape[0]
  total_follow = df2[(df2["contentId"]==df1_row["contentId"]) & df2["eventType"]=="FOLLOW"].shape[0]
  return (total_like+total_views+total_bookmark+total_commentcreated+total_follow)

df1["total_events"] = df1.apply(findtotalevent,axis = 1)
df1 = df1.sort_values(["total_events"],ascending=False)
df1.head(20)

