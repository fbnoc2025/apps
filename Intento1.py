import os

apps = {
    "spotify": r"C:\Users\User\OneDrive\Escritorio\Spotify.lnk",
    "chrome": r"C:\Users\User\OneDrive\Escritorio\Google Chrome.lnk",
    "steam": r"C:\Users\User\OneDrive\Escritorio\Steam.lnk",
    "krita": r"C:\Users\Public\Desktop\Krita.lnk",
    "obs": r"C:\Users\Public\Desktop\OBS Studio.lnk",
    "claude": r"C:\Users\User\OneDrive\Escritorio\Claude.lnk",
    "minecraft": r"C:\Users\User\OneDrive\Escritorio\Minecraft Launcher.lnk",
    "netflix": r"C:\Users\User\OneDrive\Escritorio\Netflix.lnk",
    "nitrous": r"C:\Users\User\OneDrive\Escritorio\Nitrous.lnk",
    "roblox": r"C:\Users\User\OneDrive\Escritorio\Roblox Player.lnk",
    "whatsapp": r"C:\Users\User\OneDrive\Escritorio\WhatsApp.lnk"
}

nombre = input("¿Que app quieres abrir? ").lower()

if nombre in apps:
    os.startfile(apps[nombre])
    print("Abriendo", nombre)
else:
    print("No has ingresado la app .-.")