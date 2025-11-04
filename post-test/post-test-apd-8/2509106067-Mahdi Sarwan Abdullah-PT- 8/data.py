data_pengguna = {
    "user_admin" : ["admin"],
    "pw_admin" : ["admin123"],
    "user_biasa" : ["mahdi"],
    "pw_biasa" : ["067"]
}

data_pemain = {
    "gk_utama" : ["Marten Paes"],
    "df_utama" : ["Jay Idzes",
                  "Rizky Ridho",
                  "Justin Hubner", 
                  "Calvin Verdonk", 
                  "Kevin Diks"
                  ],
    "mf_utama" : ["Thom Haye",
                  "Joel Pelupessy", 
                  "Marselino"
                  ],
    "fw_utama" : ["Rafael Struick",
                  "Ole Romeny"
                  ],
    "gk_cadangan" : ["Emil Audero",
                     "Nadeo Argawinata"
                     ],
    "df_cadangan" : ["Mees Hilgers",
                     "Sandy Walsh",
                     "Yakob Sayuri",
                     "Yance Sayuri",
                     "Justin Hubner"
                     ],
    "mf_cadangan" : ["Ivar Jenner",
                     "Ricky Kambuaya"
                     ],
    "fw_cadangan" : ["Ragnar Oratmangoen",
                     "Miliano Jonathans",
                     "Egy Maulana Vikry"
                     ],
}

semua_pemain = data_pemain["gk_utama"] + data_pemain["df_utama"] + data_pemain["mf_utama"] + data_pemain["fw_utama"] + data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"] + data_pemain["fw_cadangan"]
cek_pemain = set(semua_pemain)
