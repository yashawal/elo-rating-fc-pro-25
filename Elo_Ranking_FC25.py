import pandas as pd
from collections import defaultdict

# Initialize player ratings with defaultdict
initial_rating = 1000
k_factor = 32
players = defaultdict(lambda: initial_rating)

# Function to update Elo ratings
def update_elo(player_a, player_b, score_a, score_b):
    rating_a = players[player_a]
    rating_b = players[player_b]
    
    # Calculate expected scores - compute once and reuse
    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    expected_b = 1 - expected_a  # Mathematical relationship instead of recalculating
    
    # Calculate actual scores more efficiently
    actual_a = 0.5  # Default for draw
    if score_a > score_b:
        actual_a = 1.0
    elif score_a < score_b:
        actual_a = 0.0
    actual_b = 1.0 - actual_a  # Leverage mathematical relationship
    
    # Update ratings
    players[player_a] += k_factor * (actual_a - expected_a)
    players[player_b] += k_factor * (actual_b - expected_b)

# Function to display rankings
def display_rankings(verbose=False):
    if not players:
        if verbose:
            print("No player data found.")
        return None
        
    # Create DataFrame using vectorized operations
    standings = pd.DataFrame(list(players.items()), columns=["Player", "Rating"])
    standings["Rating"] = standings["Rating"].round(2)
    standings = standings.sort_values(by="Rating", ascending=False)
    standings.index = pd.RangeIndex(start=1, stop=len(standings)+1)  # More efficient indexing
    
    if verbose:
        pd.set_option('display.max_rows', None)
        print("\nFinal Standings:")
        print(standings)
    
    return standings

# Match results
matches = [
    ("Stingrayjnr", 10, "FacuCowen", 2),
    ("Brice", 2, "AgitPower", 3),
    ("Tekkz", 5, "KTzn", 7),
    ("Lukas", 3, "GuiBarros10", 5),
    ("NiKSNEB", 2, "LJR Peixoto", 5),
    ("Jonny", 2, "Bandar", 5),
    ("levyfinn", 7, "Montaxer", 6),
    ("Mark11", 0, "Abu Makkah", 4),
    ("Paulo Neto", 8, "Umut", 6),
    ("ManuBachoore", 4, "Obrun", 7),
    ("Giobundyy", 6, "Dylan Campbell", 5),
    ("Fouma", 2, "Tom Leese", 1),
    ("Chaaserr", 0, "Ilian", 2),
    ("K1John", 3, "Gueric10", 4),
    ("Jooelr21", 6, "ValenMz", 2),
    ("LUCA-NR1", 0, "HHezerS", 2),
    ("Dudu27", 3, "nicolas99fc", 4),
    ("seanldw", 3, "Bartz", 1),
    ("The1OS", 4, "TimoX", 4),
    ("MUAE14", 3, "iMertAL", 7),
    ("Neat", 7, "BerkayLion", 4),
    ("AboFawzi", 2, "Giuliano", 1),
    ("Obrun", 4, "Gueric10", 2),
    ("Montaxer", 0, "FacuCowen", 4),
    ("levyfinn", 0, "The1OS", 2),
    ("Abu Makkah", 9, "Brice", 2),
    ("Obrun", 4, "FacuCowen", 2),
    ("The1OS", 5, "Abu Makkah", 3),
    ("Gueric10", 3, "Montaxer", 4),
    ("levyfinn", 3, "Brice", 4),
    ("Abu Makkah", 3, "Montaxer", 0),
    ("FacuCowen", 3, "Brice", 2),
    ("Paulo Neto", 3, "seanldw", 2),
    ("Tekkz", 3, "NiKSNEB", 5),
    ("Bandar", 6, "Giobundyy", 5),
    ("KTzn", 8, "AboFawzi", 1),
    ("Paulo Neto", 1, "NiKSNEB", 3),
    ("Bandar", 2, "KTzn", 6),
    ("seanldw", 3, "Tekkz", 3),
    ("Giobundyy", 3, "AboFawzi", 7),
    ("Bandar", 2, "Tekkz", 6),
    ("Paulo Neto", 3, "AboFawzi", 1),
    ("LJR Peixoto", 6, "Fouma", 5),
    ("Mark11", 2, "Neat", 0),
    ("GuiBarros10", 5, "Jonny", 4),
    ("AgitPower", 2, "Ilian", 2),
    ("LJR Peixoto", 3, "Mark11", 1),
    ("GuiBarros10", 4, "Ilian", 3),
    ("Fouma", 5, "Neat", 4),
    ("Jonny", 2, "AgitPower", 4),
    ("Ilian", 2, "Fouma", 4),
    ("Mark11", 4, "AgitPower", 1),
    ("Umut", 3, "iMertAL", 2),
    ("Lukas", 2, "nicolas99fc", 5),
    ("ManuBachoore", 5, "HHezerS", 3),
    ("Stingrayjnr", 4, "Jooelr21", 2),
    ("Umut", 1, "nicolas99fc", 4),
    ("ManuBachoore", 2, "Stingrayjnr", 3),
    ("iMertAL", 9, "Lukas", 0),
    ("HHezerS", 7, "Jooelr21", 3),
    ("ManuBachoore", 4, "iMertAL", 0),
    ("Umut", 6, "HHezerS", 6),
    ("Montaxer", 4, "iMertAL", 4),
    ("AboFawzi", 7, "AgitPower", 1),
    ("iMertAL", 4, "AboFawzi", 7),
    ("Jafonso", 5, "NiKSNEB", 2),
    ("xcharifx", 4, "Mark11", 4),
    ("FacuCowen", 4, "Stingrayjnr", 5),
    ("xcharifx", 2, "Jafonso", 5),
    ("FacuCowen", 0, "NiKSNEB", 3),
    ("Stingrayjnr", 3, "Mark11", 2),
    ("FacuCowen", 5, "Jafonso", 3),
    ("Stingrayjnr", 4, "xcharifx", 3),
    ("Mark11", 2, "NiKSNEB", 4),
    ("Jafonso", 6, "Stingrayjnr", 1),
    ("Mark11", 3, "FacuCowen", 2),
    ("NiKSNEB", 2, "xcharifx", 3),
    ("Jafonso", 4, "Mark11", 1),
    ("NiKSNEB", 3, "Stingrayjnr", 2),
    ("xcharifx", 3, "FacuCowen", 4),
    ("Mark11", 3, "Jafonso", 3),
    ("Stingrayjnr", 6, "NiKSNEB", 2),
    ("FacuCowen", 3, "xcharifx", 3),
    ("NiKSNEB", 2, "Jafonso", 3),
    ("Mark11", 1, "xcharifx", 2),
    ("Stingrayjnr", 4, "FacuCowen", 3),
    ("Jafonso", 1, "FacuCowen", 3),
    ("xcharifx", 2, "Stingrayjnr", 8),
    ("NiKSNEB", 2, "Mark11", 4),
    ("Jafonso", 5, "xcharifx", 3),
    ("NiKSNEB", 1, "FacuCowen", 1),
    ("Mark11", 3, "Stingrayjnr", 4),
    ("Stingrayjnr", 7, "Jafonso", 1),
    ("FacuCowen", 4, "Mark11", 1),
    ("xcharifx", 3, "NiKSNEB", 2),
    ("The1OS", 4, "Vejrgang", 4),
    ("LJR Peixoto", 5, "nicolas99fc", 4),
    ("AboFawzi", 3, "ManuBachoore", 5),
    ("Vejrgang", 5, "nicolas99fc", 3),
    ("The1OS", 3, "ManuBachoore", 3),
    ("LJR Peixoto", 5, "AboFawzi", 3),
    ("LJR Peixoto", 2, "Vejrgang", 3),
    ("AboFawzi", 3, "The1OS", 1),
    ("ManuBachoore", 1, "nicolas99fc", 1),
    ("Vejrgang", 7, "AboFawzi", 1),
    ("ManuBachoore", 4, "LJR Peixoto", 1),
    ("nicolas99fc", 7, "The1OS", 0),
    ("Vejrgang", 2, "ManuBachoore", 4),
    ("nicolas99fc", 2, "AboFawzi", 1),
    ("The1OS", 3, "LJR Peixoto", 5),
    ("Obrun", 3, "Emre Yilmaz", 3),
    ("Umut", 4, "Yuval", 2),
    ("GuiBarros10", 2, "Tekkz", 4),
    ("Emre Yilmaz", 3, "GuiBarros10", 2),
    ("Tekkz", 3, "Umut", 3),
    ("Yuval", 2, "Obrun", 2),
    ("Emre Yilmaz", 4, "Tekkz", 1),
    ("Yuval", 1, "GuiBarros10", 2),
    ("Obrun", 7, "Umut", 2),
    ("Yuval", 5, "Emre Yilmaz", 4),
    ("Obrun", 3, "Tekkz", 2),
    ("Umut", 3, "GuiBarros10", 5),
    ("Emre Yilmaz", 2, "Umut", 4),
    ("GuiBarros10", 2, "Obrun", 3),
    ("Tekkz", 4, "Yuval", 5),
    ("Abu Makkah", 2, "PHzin", 0),
    ("Fouma", 3, "Levi de Weerd", 3),
    ("Paulo Neto", 6, "KTzn", 2),
    ("Levi de Weerd", 4, "PHzin", 3),
    ("Abu Makkah", 8, "KTzn", 0),
    ("Fouma", 5, "Paulo Neto", 3),
    ("PHzin", 6, "KTzn", 1),
    ("Levi de Weerd", 1, "Paulo Neto", 1),
    ("Abu Makkah", 6, "Fouma", 1),
    ("PHzin", 4, "Fouma", 4),
    ("Paulo Neto", 4, "Abu Makkah", 5),
    ("KTzn", 7, "Levi de Weerd", 3),
    ("PHzin", 6, "Paulo Neto", 4),
    ("KTzn", 1, "Fouma", 6),
    ("Levi de Weerd", 5, "Abu Makkah", 1),
    ("Abu Makkah", 5, "Adam Hatake", 3),
    ("Umut", 6, "Jay", 2),
    ("ManuBachoore", 6, "The1OS", 0),
    ("Tekkz", 8, "ibra", 2),
    ("Young", 5, "Bartz", 6),
    ("Fouma", 5, "Funino", 3),
    ("HHezerS", 5, "Perkkix", 4),
    ("levyfinn", 5, "Chaaserr", 6),
    ("K1John", 5, "Kaylan", 3),
    ("GuiBarros10", 6, "DivineCS7", 3),
    ("Mark11", 5, "cone1996fc", 3),
    ("Montaxer", 5, "LUCA-NR1", 0),
    ("FacuCowen", 5, "Joksan", 4),
    ("Lukas", 5, "didychrislito", 0),
    ("Dudu27", 4, "Collin", 3),
    ("Neat", 2, "Jooelr21", 1),
    ("Paulo Neto", 6, "ValenMz", 2),
    ("Giuliano", 4, "KTzn", 6),
    ("AboFawzi", 5, "iMertAL", 3),
    ("AgitPower", 7, "TimoX", 1),
    ("Stingrayjnr", 2, "MarwanMC9", 1),
    ("BerkayLion", 5, "Giobundyy", 1),
    ("Brice", 3, "NiKSNEB", 4),
    ("AHMADALS", 3, "Gercrack30", 4),
    ("Bandar", 5, "LJR Peixoto", 5),
    ("Web Nasri", 2, "Ilian", 3),
    ("Obrun", 5, "MUAE14", 2),
    ("H1dalgo", 5, "Gueric10", 1),
    ("Happy", 4, "Dylan Campbell", 2),
    ("seanldw", 1, "Tom Leese", 2),
    ("iMertAL", 4, "Young", 2),
    ("AHMADALS", 1, "LUCA-NR1", 0),
    ("DivineCS7", 1, "levyfinn", 8),
    ("Web Nasri", 1, "Brice", 2),
    ("Joksan", 3, "The1OS", 4),
    ("MUAE14", 2, "Eggsy", 0),
    ("Giuliano", 6, "Jooelr21", 6),
    ("cone1996fc", 6, "Kaylan", 4),
    ("Giobundyy", 8, "didychrislito", 3),
    ("ibra", 4, "seanldw", 3),
    ("Perkkix", 2, "Gueric10", 4),
    ("TimoX", 3, "Collin", 3),
    ("Dylan Campbell", 6, "Adam Hatake", 3),
    ("Funino", 2, "Bandar", 6),
    ("Jay", 1, "MarwanMC9", 5),
    ("H1dalgo", 1, "LJR Peixoto", 2),
    ("ManuBachoore", 9, "Bartz", 2),
    ("Dudu27", 3, "FacuCowen", 3),
    ("K1John", 1, "Neat", 3),
    ("Tom Leese", 3, "AgitPower", 6),
    ("KTzn", 7, "BerkayLion", 6),
    ("Fouma", 2, "Mark11", 4),
    ("Tekkz", 2, "Obrun", 8),
    ("Ilian", 3, "GuiBarros10", 5),
    ("Happy", 2, "HHezerS", 7),
    ("Gercrack30", 4, "Paulo Neto", 5),
    ("AboFawzi", 2, "Lukas", 6),
    ("Umut", 6, "Stingrayjnr", 5),
    ("Montaxer", 2, "Jonny", 1),
    ("nicolas99fc", 2, "Abu Makkah", 3),
    ("NiKSNEB", 2, "Chaaserr", 2),
    ("HHezerS", 3, "Umut", 5),
    ("Chaaserr", 0, "ManuBachoore", 3),
    ("Paulo Neto", 5, "GuiBarros10", 4),
    ("Abu Makkah", 1, "LJR Peixoto", 4),
    ("FacuCowen", 0, "KTzn", 5),
    ("Neat", 2, "Mark11", 3),
    ("Montaxer", 0, "Lukas", 2),
    ("AgitPower", 1, "Obrun", 8),
    ("Collin", 5, "Adam Hatake", 2),
    ("Web Nasri", 2, "Eggsy", 6),
    ("Jay", 1, "Kaylan", 3),
    ("Perkkix", 3, "Joksan", 2),
    ("seanldw", 3, "didychrislito", 1),
    ("Young", 5, "DivineCS7", 5),
    ("LUCA-NR1", 4, "Funino", 2),
    ("levyfinn", 2, "The1OS", 1),
    ("nicolas99fc", 5, "TimoX", 3),
    ("H1dalgo", 4, "Brice", 4),
    ("Gercrack30", 2, "K1John", 5),
    ("Giobundyy", 8, "ValenMz", 2),
    ("Dudu27", 5, "Tom Leese", 1),
    ("AboFawzi", 3, "Ilian", 4),
    ("ibra", 1, "BerkayLion", 4),
    ("Happy", 2, "MUAE14", 4),
    ("Bandar", 6, "Bartz", 3),
    ("Stingrayjnr", 6, "cone1996fc", 2),
    ("Jonny", 8, "MarwanMC9", 4),
    ("Tekkz", 8, "Dylan Campbell", 1),
    ("Gueric10", 2, "NiKSNEB", 4),
    ("Fouma", 2, "Jooelr21", 6),
    ("iMertAL", 3, "AHMADALS", 2),
    ("LJR Peixoto", 4, "Paulo Neto", 4),
    ("Lukas", 0, "Umut", 6),
    ("ManuBachoore", 6, "KTzn", 2),
    ("Obrun", 2, "Mark11", 2),
    ("Ilian", 2, "Montaxer", 4),
    ("Dudu27", 4, "Jonny", 5),
    ("K1John", 1, "Abu Makkah", 5),
    ("Brice", 7, "Jooelr21", 0),
    ("Chaaserr", 3, "Stingrayjnr", 4),
    ("BerkayLion", 2, "AgitPower", 7),
    ("Giobundyy", 3, "GuiBarros10", 5),
    ("NiKSNEB", 5, "MUAE14", 2),
    ("Tekkz", 5, "HHezerS", 3),
    ("iMertAL", 1, "levyfinn", 3),
    ("Bandar", 5, "nicolas99fc", 2),
    ("FacuCowen", 3, "Neat", 1),
    ("Happy", 1, "Tom Leese", 3),
    ("Gueric10", 4, "Collin", 3),
    ("Fouma", 3, "AHMADALS", 1),
    ("ibra", 4, "Dylan Campbell", 4),
    ("DivineCS7", 2, "LUCA-NR1", 3),
    ("MarwanMC9", 1, "Bartz", 3),
    ("Giuliano", 5, "H1dalgo", 2),
    ("Gercrack30", 4, "The1OS", 6),
    ("Kaylan", 2, "AboFawzi", 3),
    ("ValenMz", 8, "cone1996fc", 0),
    ("Eggsy", 3, "TimoX", 4),
    ("seanldw", 6, "Perkkix", 0),
    ("ManuBachoore", 1, "Vejrgang", 6),
    ("AboFawzi", 2, "nicolas99fc", 5),
    ("LJR Peixoto", 3, "The1OS", 0),
    ("AboFawzi", 7, "Vejrgang", 7),
    ("LJR Peixoto", 7, "ManuBachoore", 3),
    ("The1OS", 0, "nicolas99fc", 3),
    ("Vejrgang", 7, "LJR Peixoto", 3),
    ("The1OS", 0, "AboFawzi", 3),
    ("nicolas99fc", 5, "ManuBachoore", 1),
    ("nicolas99fc", 2, "Vejrgang", 2),
    ("ManuBachoore", 3, "The1OS", 0),
    ("AboFawzi", 3, "LJR Peixoto", 4),
    ("Vejrgang", 3, "The1OS", 0),
    ("nicolas99fc", 6, "LJR Peixoto", 1),
    ("ManuBachoore", 7, "AboFawzi", 4),
    ("Emre Yilmaz", 3, "Yuval", 2),
    ("Tekkz", 5, "Obrun", 3),
    ("GuiBarros10", 4, "Umut", 3),
    ("Umut", 4, "Emre Yilmaz", 9),
    ("Obrun", 3, "GuiBarros10", 1),
    ("Yuval", 6, "Tekkz", 3),
    ("Tekkz", 5, "Emre Yilmaz", 6),
    ("GuiBarros10", 3, "Yuval", 4),
    ("Umut", 5, "Obrun", 7),
    ("GuiBarros10", 2, "Emre Yilmaz", 4),
    ("Umut", 5, "Tekkz", 2),
    ("Obrun", 3, "Yuval", 3),
    ("Emre Yilmaz", 4, "Obrun", 5),
    ("Yuval", 7, "Umut", 4),
    ("Tekkz", 4, "GuiBarros10", 6),   
]

# Main function to process matches and display rankings
def main():
    # Process all matches in bulk
    print("Processing matches...")
    for player_a, score_a, player_b, score_b in matches:
        update_elo(player_a, player_b, score_a, score_b)
    
    # Display final standings
    standings = display_rankings(verbose=False)
    
    # Export to CSV if needed
    standings.to_csv("elo_rankings.csv", index_label="Rank")
    print(f"Rankings exported to elo_rankings.csv")
    
    # Show top 50 players
    print(f"\nTop 50 Players:")
    print(standings.head(50))
    
    return standings

# Run the main function if script is executed directly
if __name__ == "__main__":
    main()