import streamlit as st
import pandas as pd
from PIL import Image
import os
import sys

#st.title("Data collection of energy conversion and storage systems")
img2 = Image.open(r"C:\Users\adeba\Downloads\aww_logo.png")
own_page_config = {"page_title":"Data collection of energy conversion and storage systems", "page_icon":img2,"layout":"wide" }
st.set_page_config(**own_page_config)


@st.cache
def convert_file(file):
    return file.to_csv().encode('utf-8')

def my_custom_sort(tech):
    #sorts the energy conversion technologies in this order
    custom_order = ['solar', 'biomass', 'wind', 'biogas', 'gas', 'geothermal', 'steam (hydro)']
    if tech in custom_order:
        return custom_order.index(tech)
    else:
        return len(custom_order)


#display data
energy = pd.read_excel(r"C:\Users\adeba\OneDrive\Desktop\Masters Thesis\Uniform_energy.xlsx")#
energy = energy.drop(columns="entry_id")


energy_conv = list(energy['energy conversion source'].unique())
energy_conv.sort(key=my_custom_sort)


with st.expander("Energy conversion technologies"):    

        conv_new = st.radio("Select and energy conversion source", ("solar", "biomass", "wind", "biogas", "gas", "geothermal", "steam (hydro)", "hydro"))
        if conv_new == "solar":
            techno = st.radio("Select a technology", ("all", "photovoltaic panel", "PVT (photovoltaic-thermal hybrid solar collector)", "heat collector (flat)",\
                             "heat collector (evacuated tube)"), horizontal= True)
            if techno == "all":
                c_s = energy[energy['energy conversion source'] == "solar"].dropna(axis=1, how='all')
                st.dataframe(c_s)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_s.describe())
                
            elif techno == "photovoltaic panel":
                c_s = energy[energy['energy conversion source'] == "solar"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "photovoltaic panel"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe()) 

            elif techno == "PVT (photovoltaic-thermal hybrid solar collector)":
                c_s = energy[energy['energy conversion source'] == "solar"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "PVT (photovoltaic-thermal hybrid solar collector)"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())  

            elif techno == "heat collector (flat)":
                c_s = energy[energy['energy conversion source'] == "solar"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "heat collector (flat)"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())  

            elif techno == "heat collector (evacuated tube)":
                c_s = energy[energy['energy conversion source'] == "solar"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "heat collector (evacuated tube)"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())    


        elif conv_new == "biomass":
            st.write("Technology available in dataframe : boiler")
            c_s = energy[energy['energy conversion source'] == "biomass"].dropna(axis=1, how='all')
            st.dataframe(c_s)
            stat = st.checkbox("dataframe statistics",value=False)
            if stat:
                st.success("Here's some dataframe statistics")
                st.table(c_s.describe())

        elif conv_new == "wind":
            st.write("Technology available in dataframe : turbine")
            c_s = energy[energy['energy conversion source'] == "wind"].dropna(axis=1, how='all')
            st.dataframe(c_s)
            stat = st.checkbox("dataframe statistics",value=False)
            if stat:
                st.success("Here's some dataframe statistics")
                st.table(c_s.describe())

        elif conv_new == "biogas":
            techno = st.radio("Select a technology", ("all", "turbine", "generator", "CHP generator"), horizontal= True)
            if techno == "all":
                c_s = energy[energy['energy conversion source'] == "biogas"].dropna(axis=1, how='all')
                st.dataframe(c_s)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_s.describe())

            elif techno == "turbine":
                c_s = energy[energy['energy conversion source'] == "biogas"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "turbine"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())

            elif techno == "generator":
                c_s = energy[energy['energy conversion source'] == "biogas"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "generator"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())

            elif techno == "CHP generator":
                c_s = energy[energy['energy conversion source'] == "biogas"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "CHP generator"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())

        elif conv_new == "gas":
            techno = st.radio("Select a technology", ("all", "turbine", "generator", "CHP generator"), horizontal= True)
            if techno == "all":
                c_s = energy[energy['energy conversion source'] == "gas"].dropna(axis=1, how='all')
                st.dataframe(c_s)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_s.describe())

            elif techno == "turbine":
                c_s = energy[energy['energy conversion source'] == "gas"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "turbine"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())

            elif techno == "generator":
                c_s = energy[energy['energy conversion source'] == "gas"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "generator"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())

            elif techno == "CHP generator":
                c_s = energy[energy['energy conversion source'] == "gas"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "CHP generator"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())

        elif conv_new == "geothermal":
            st.write("Technology available in dataframe : turbine")
            c_s = energy[energy['energy conversion source'] == "geothermal"].dropna(axis=1, how='all')
            st.dataframe(c_s)
            stat = st.checkbox("dataframe statistics",value=False)
            if stat:
                st.success("Here's some dataframe statistics")
                st.table(c_s.describe()) 

        elif conv_new == "steam (hydro)":
            techno = st.radio("Select a technology", ("all", "turbine/generator", "turbine"), horizontal= True)
            if techno == "all":
                c_s = energy[energy['energy conversion source'] == "steam (hydro)"].dropna(axis=1, how='all')
                st.dataframe(c_s)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_s.describe())

            elif techno == "turbine/generator":
                c_s = energy[energy['energy conversion source'] == "steam (hydro)"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "turbine/generator"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())

            elif techno == "turbine":
                c_s = energy[energy['energy conversion source'] == "steam (hydro)"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "turbine"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())

        elif conv_new == "hydro":
            techno = st.radio("Select a technology", ("all", "turbine", "generator"), horizontal= True)
            if techno == "all":
                c_s = energy[energy['energy conversion source'] == "hydro"].dropna(axis=1, how='all')
                st.dataframe(c_s)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_s.describe())

            elif techno == "turbine":
                c_s = energy[energy['energy conversion source'] == "hydro"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "turbine"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe())

            elif techno == "generator":
                c_s = energy[energy['energy conversion source'] == "hydro"].dropna(axis=1, how='all')
                c_t = c_s[c_s['technology'] == "generator"].dropna(axis=1, how='all')
                st.dataframe(c_t)
                stat = st.checkbox("dataframe statistics",value=False)
                if stat:
                    st.success("Here's some dataframe statistics")
                    st.table(c_t.describe()) 

##################################################################################################

#################################################################################################

storage = pd.read_excel(r"C:\Users\adeba\OneDrive\Desktop\Masters Thesis\Uniform_energy.xlsx", sheet_name='storage')
storage =storage.drop(columns="entry_id")

with st.expander("Energy storage technologies"):
        energy_store = storage['energy storage technology'].unique()       
        for store in energy_store:
            if st.button(store, key = store):
                stort = store
                c_storage = storage[storage['energy storage technology'] == stort].dropna(axis=1, how='all') 
                st.dataframe(c_storage)
                st.write(len(c_storage.columns))

# insert power-BI report:
with st.expander("Data Visualization"):
    st.markdown('<iframe title="Energy" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=b33dfa9f-b2c5-4237-8c6f-3f494812ee8c&autoAuth=true&ctid=ed4afd5e-468f-46b7-ab2e-dda54017f421" \
                frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

with st.expander("save files"):
    choice = st.selectbox("choose technology", options=['energy conversion', 'energy storage', "combo" ,"all"])
    if choice == 'energy conversion':
        source_choice = st.multiselect("select source", energy['energy conversion source'].unique(), default=None)
        source_choice = list(source_choice)
        dataf = energy[energy['energy conversion source'].isin(source_choice)].dropna(axis=1, how='all').reset_index(drop=True)
        if dataf is not None:
            csv = convert_file(dataf.reset_index(drop=True))
            st.dataframe(dataf.head())
            st.download_button(label="Download data as csv", data=csv, file_name='energy_conversion/storage_data.csv', mime= 'text/csv') 




    elif choice == 'energy storage':
        storage_choice = st.multiselect("select technology",storage['energy storage technology'].unique())
        storage_choice = list(storage_choice)
        dataf= storage[storage['energy storage technology'].isin(storage_choice)].dropna(axis=1, how='all')
        if dataf is not None:
            csv = convert_file(dataf.reset_index(drop=True))
            st.dataframe(dataf.head())
            st.download_button(label="Download data as csv", data=csv, file_name='energy_conversion/storage_data.csv', mime= 'text/csv')
    
    elif choice == "combo":
        combo_list = list(energy['energy conversion source'].unique()) + list(storage['energy storage technology'].unique())
        combo_choice = st.multiselect("select conversion source and storage technology", combo_list)
        tempC = list(set(combo_choice) & set(energy['energy conversion source'].unique()))
        tempS = list(set(combo_choice) & set(storage['energy storage technology'].unique()))

        combo_conversion = energy[energy['energy conversion source'].isin(tempC)]
        combo_storage = storage[storage['energy storage technology'].isin(tempS)]
        dataf= combo_conversion.append(combo_storage)
        if dataf is not None:
            csv = convert_file(dataf.reset_index(drop=True))
            st.dataframe(dataf.head())
            st.download_button(label="Download data as csv", data=csv, file_name='energy_conversion/storage_data.csv', mime= 'text/csv')


    elif choice == "all":
        all = energy.append(storage, sort=False).reset_index(drop=True)
        if all is not None:
            st.dataframe(all.head())
            csv = convert_file(all)
            st.download_button(label="Download data as csv", data=csv, file_name='energy_conversion/storage_data.csv', mime= 'text/csv')
        
    else:
        st.expander("save files")

