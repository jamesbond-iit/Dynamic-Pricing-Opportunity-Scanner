import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Dynamic Pricing Opportunity Scanner",layout="wide")
@st.cache_data
def load():
 df=pd.read_csv("data/pricing_sales_data.csv",parse_dates=["date"]); opp=pd.read_csv("docs/product_pricing_opportunities.csv"); return df,opp
df,opp=load(); st.title("Dynamic Pricing Opportunity Scanner"); st.caption("Pricing analytics for demand, margin, competitive positioning and revenue scenarios.")
with st.sidebar:
 cats=st.multiselect("Category",sorted(df.category.unique()),default=sorted(df.category.unique())); chans=st.multiselect("Channel",sorted(df.channel.unique()),default=sorted(df.channel.unique())); segs=st.multiselect("Customer Segment",sorted(df.customer_segment.unique()),default=sorted(df.customer_segment.unique()))
f=df[df.category.isin(cats)&df.channel.isin(chans)&df.customer_segment.isin(segs)]
rev=f.revenue.sum(); gp=f.gross_profit.sum(); units=f.units_sold.sum(); margin=100*gp/rev; gap=f.price_gap_pct.mean()
a,b,c,d,e=st.columns(5); a.metric("Revenue",f"₹{rev/1e6:.2f}M"); b.metric("Gross Profit",f"₹{gp/1e6:.2f}M"); c.metric("Units Sold",f"{units:,.0f}"); d.metric("Gross Margin",f"{margin:.1f}%"); e.metric("Avg Competitor Gap",f"{gap:.1f}%")
cat=f.groupby("category",as_index=False).agg(revenue=("revenue","sum"),profit=("gross_profit","sum")); st.plotly_chart(px.bar(cat,x="category",y="revenue",text_auto=".3s",title="Revenue by Category"),use_container_width=True)
p=f.groupby(["product_id","category"],as_index=False).agg(price_gap_pct=("price_gap_pct","mean"),elasticity=("baseline_elasticity","mean"),units=("units_sold","sum")); st.plotly_chart(px.scatter(p,x="price_gap_pct",y="elasticity",size="units",color="category",hover_data=["product_id"],title="Competitive Price Gap vs Elasticity"),use_container_width=True)
action=opp.recommended_action.value_counts().reset_index(); action.columns=["action","products"]; st.plotly_chart(px.bar(action,x="action",y="products",text_auto=True,title="Recommended Pricing Actions"),use_container_width=True)
st.subheader("Top Pricing Opportunities"); cols=["product_id","category","avg_price","avg_competitor_price","price_gap_pct","avg_elasticity","current_margin_pct","recommended_action","revenue_change","opportunity_score"]; st.dataframe(opp[cols].head(20),use_container_width=True,hide_index=True)
sc=pd.read_csv("docs/price_scenarios.csv"); sc["price_change_pct"]=100*sc.price_change; ss=sc.groupby("price_change_pct",as_index=False).revenue_change.sum(); st.plotly_chart(px.bar(ss,x="price_change_pct",y="revenue_change",title="Portfolio Revenue Change Under Price Scenarios",labels={"price_change_pct":"Price Change (%)","revenue_change":"Simulated Revenue Change"}),use_container_width=True)
st.info("Simulations are directional estimates. Validate material pricing changes with controlled experiments and margin constraints before implementation.")