import win32com.client
import pythoncom

def generate_com_cache():
    try:
        pythoncom.CoInitialize()
        print("Iniciando la generación de la caché COM...")
        vissim = win32com.client.gencache.EnsureDispatch("Vissim.Vissim")
        print("VISSIM COM classes generated successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pythoncom.CoUninitialize()

if __name__ == "__main__":
    generate_com_cache()
