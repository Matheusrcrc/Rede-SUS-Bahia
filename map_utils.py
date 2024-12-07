
import folium
from folium import plugins

def create_base_map(center_lat=-12.5, center_lon=-41.7, zoom=6):
    '''Create a base map centered on Bahia'''
    return folium.Map(location=[center_lat, center_lon], 
                     zoom_start=zoom,
                     tiles='CartoDB positron')

def add_health_unit_markers(m, df):
    '''Add markers for health units to the map'''
    for idx, row in df.iterrows():
        popup_text = f'''
            <div style="font-family: Arial; width: 200px;">
                <h4>{row['regiao']}</h4>
                <b>Unidades:</b><br>
                - USB: {row['n_usb']}<br>
                - USA: {row['n_usa']}<br>
                - UPA: {row['n_upa']}<br>
                - PA: {row['n_pa']}<br>
                <br>
                <b>Cobertura SAMU:</b> {row['cobertura_samu']:.1f}%<br>
                <b>Cobertura AB:</b> {row['cobertura_atencao_basica']:.1f}%
            </div>
        '''
        
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
    
    return m

def add_heatmap(m, df):
    '''Add heatmap layer based on unit distribution'''
    heat_data = [[row['lat'], row['lon'], row['n_usb'] + row['n_usa']] 
                 for idx, row in df.iterrows()]
    
    plugins.HeatMap(heat_data).add_to(m)
    return m
