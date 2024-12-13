import requests

class NIST_API():
    def __init__():
        pass

    @staticmethod
    def get_website_content(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            return None
    
    @staticmethod
    def get_density(temp: float, pres:float):
        """Get the density of xenon at a given temperature and pressure.
        Temperature is in Celsius and pressure is in bar."""

        p_low = p_high = pres
        p_inc = 0
        temp_C = temp

        nist_url_start = f'https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7440633&Type=IsoTherm&Digits=10&'
        nist_url_pressure = f'PLow={p_low}&PHigh={p_high}&PInc={p_inc}&'
        nist_url_temp = f'T={temp_C}&'
        nist_url_end = f'RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm'

        nist_url = nist_url_start + nist_url_pressure + nist_url_temp + nist_url_end

        nist_text = get_website_content(nist_url)
        if nist_text is None:
            raise ValueError("Failed to fetch NIST data")
        else:
            density = nist_text.split()[32]
            return float(density)
