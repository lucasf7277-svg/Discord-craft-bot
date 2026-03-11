import discord
from discord.ext import commands
from discord.ui import View, Select
import math
import os

TOKEN = "MTQ4MDM4MjIyNzQ0MjU2NTE2Mg.GyJdIA.OE-ApaOP6xwYmW5bz80FyRQEMyfNlFDMELSEhc"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# LOCAIS
# =========================

locais_craft = {
    "Craft Geral": "CP 941",
    "Laboratório": "CP 1016",
    "Siderurgia": "CP 174",
    "Reciclagem": "CP 3021",
    "Carregadores": "CP 934",
    "Peças de Arma": "CP 1053",
    "Armas Leves": "CP 3001",
    "Armas Pesadas": "CP 1007"
}

# =========================
# RECEITAS
# =========================

receitas_craft = {

"copo_cartao":{
"local":"Craft Geral",
"lote":1,
"materiais":{"cartao":2}
},

"saco_plastico":{
"local":"Craft Geral",
"lote":5,
"materiais":{"plastico":2}
},

"radio":{
"local":"Craft Geral",
"lote":1,
"materiais":{
"abs":5,
"borracha":10,
"restos_eletronicos":10
}
},

"tesoura":{
"local":"Craft Geral",
"lote":1,
"materiais":{
"pedaco_de_metal":5,
"plastico":10
}
},

"lata_vazia":{
"local":"Craft Geral",
"lote":1,
"materiais":{"aluminio":3}
},

"saco_ginasio":{
"local":"Craft Geral",
"lote":1,
"materiais":{"tecido":20}
},

"rebarbadora":{
"local":"Craft Geral",
"lote":1,
"materiais":{
"abs":20,
"aluminio":40,
"aco":30,
"cobre":8
}
},

"lockpick_avancada":{
"local":"Craft Geral",
"lote":1,
"materiais":{
"aco":85,
"parafusos":5
}
},

"broca_basica":{
"local":"Craft Geral",
"lote":1,
"materiais":{
"aco":90,
"cobre":70,
"pedaco_de_metal":40
}
},

"furadora_basica":{
"local":"Craft Geral",
"lote":1,
"materiais":{
"broca_basica":1,
"mola":10,
"parafusos":10,
"plastico":200,
"restos_eletronicos":100
}
},

"jammer":{
"local":"Craft Geral",
"lote":1,
"materiais":{
"abs":20,
"borracha":20,
"prata":3,
"restos_eletronicos":10
}
},

"algemas":{
"local":"Craft Geral",
"lote":1,
"materiais":{
"aluminio":80,
"aco":50,
"mola":4,
"parafusos":8,
"prata":80
}
},

"abs":{
"local":"Laboratório",
"lote":1,
"materiais":{"fibra":1,"plastico":1}
},

"nitrato_potassio":{
"local":"Laboratório",
"lote":1,
"materiais":{
"casca_de_banana":1,
"morangos":1
}
},

"c4":{
"local":"Laboratório",
"lote":1,
"materiais":{
"abs":10,
"borracha":20,
"polvora":10,
"restos_eletronicos":8
}
},

"lingote_ferro":{
"local":"Siderurgia",
"lote":1,
"materiais":{"ferro":1}
},

"aco":{
"local":"Siderurgia",
"lote":1,
"materiais":{
"carvao":1,
"lingote_ferro":1
}
},

"bronze":{
"local":"Siderurgia",
"lote":1,
"materiais":{
"cobre":1,
"estanho":1
}
},

"fibra":{
"local":"Reciclagem",
"lote":1,
"materiais":{
"couro":2,
"pele":3
}
},

"aluminio":{
"local":"Reciclagem",
"lote":2,
"materiais":{
"estanho":2,
"tecido":2
}
},

"polimero":{
"local":"Reciclagem",
"lote":1,
"materiais":{
"nylon":1,
"vidro":1
}
},

"peca_basica":{
"local":"Peças de Arma",
"lote":2,
"materiais":{
"abs":2,
"aluminio":1,
"borracha":1,
"dinheiro_sujo":400,
"pedaco_de_metal":2
}
},

"peca_avancada":{
"local":"Peças de Arma",
"lote":2,
"materiais":{
"aluminio":1,
"aco":2,
"borracha":1,
"bronze":1,
"dinheiro_sujo":600,
"polimero":1
}
},

# =========================
# CARREGADORES
# =========================

"carregador_pistola":{
"local":"Carregadores",
"lote":2,
"materiais":{
"cobre":1,
"dinheiro_sujo":1500,
"niquel":1,
"polvora":1
}
},

"carregador_shotgun":{
"local":"Carregadores",
"lote":2,
"materiais":{
"cobre":1,
"dinheiro_sujo":1500,
"niquel":2,
"polvora":2
}
},

"carregador_smg":{
"local":"Carregadores",
"lote":2,
"materiais":{
"cobre":1,
"dinheiro_sujo":2000,
"niquel":2,
"polvora":2
}
},

"carregador_rifle":{
"local":"Carregadores",
"lote":2,
"materiais":{
"cobre":2,
"dinheiro_sujo":2500,
"niquel":2,
"polvora":3
}
},

# =========================
# ARMAS LEVES
# =========================

"fn_1922":{
"local":"Armas Leves",
"lote":1,
"materiais":{
"blueprint_pistola":12,
"dinheiro_sujo":25000,
"peca_basica":60
}
},

"ranger_12":{
"local":"Armas Leves",
"lote":1,
"materiais":{
"blueprint_shotgun":16,
"dinheiro_sujo":35000,
"peca_basica":80
}
},

"desert_eagle":{
"local":"Armas Leves",
"lote":1,
"materiais":{
"blueprint_pistola":14,
"dinheiro_sujo":30000,
"peca_basica":70
}
},

"colt_scamp":{
"local":"Armas Leves",
"lote":1,
"materiais":{
"blueprint_smg":18,
"dinheiro_sujo":40000,
"peca_basica":90
}
},

"spas_12":{
"local":"Armas Leves",
"lote":1,
"materiais":{
"blueprint_shotgun":18,
"dinheiro_sujo":42000,
"peca_basica":95
}
},

"thompson":{
"local":"Armas Leves",
"lote":1,
"materiais":{
"blueprint_smg":20,
"dinheiro_sujo":45000,
"peca_basica":100
}
},

# =========================
# ARMAS PESADAS
# =========================

"sig_pdw":{
"local":"Armas Pesadas",
"lote":1,
"materiais":{
"blueprint_rifle":20,
"dinheiro_sujo":55000,
"peca_avancada":100
}
},

"akm":{
"local":"Armas Pesadas",
"lote":1,
"materiais":{
"blueprint_rifle":22,
"dinheiro_sujo":60000,
"peca_avancada":110
}
},

"famas":{
"local":"Armas Pesadas",
"lote":1,
"materiais":{
"blueprint_rifle":22,
"dinheiro_sujo":62000,
"peca_avancada":115
}
},

"tar21":{
"local":"Armas Pesadas",
"lote":1,
"materiais":{
"blueprint_rifle":24,
"dinheiro_sujo":70000,
"peca_avancada":120
}
}
}

# =========================
# MENU
# =========================

class LocalSelect(Select):

    def __init__(self):

        options = []

        for local, cp in locais_craft.items():
            options.append(discord.SelectOption(label=f"{local} ({cp})"))

        super().__init__(placeholder="Escolhe o local", options=options)

    async def callback(self, interaction: discord.Interaction):

        local_label = self.values[0]
        local = local_label.split(" (")[0]

        options = []

        for item, data in receitas_craft.items():
            if data["local"] == local:
                options.append(discord.SelectOption(label=item))

        view = View()
        view.add_item(CraftSelect(options))

        await interaction.response.send_message(
            f"Crafts em **{local}**",
            view=view,
            ephemeral=True
        )


class CraftSelect(Select):

    def __init__(self, options):
        super().__init__(placeholder="Escolhe o craft", options=options)

    async def callback(self, interaction: discord.Interaction):

        item = self.values[0]

        await interaction.response.send_message(
            f"Usa:\n`!craft {item} quantidade`",
            ephemeral=True
        )


class ReceitaMenu(View):

    def __init__(self):
        super().__init__()
        self.add_item(LocalSelect())

# =========================
# COMANDOS
# =========================

@bot.event
async def on_ready():
    print(f"Bot ligado como {bot.user}")


@bot.command()
async def receitas(ctx):

    view = ReceitaMenu()

    await ctx.reply(
        "Escolhe o local de craft:",
        view=view
    )


@bot.command()
async def locais(ctx):

    msg = "**LOCAIS DE CRAFT**\n\n"

    for nome, cp in locais_craft.items():
        msg += f"{nome} → {cp}\n"

    await ctx.send(msg)


@bot.command()
async def craft(ctx, item, quantidade: int = 1):

    item = item.lower()

    if item not in receitas_craft:
        await ctx.send("Receita não encontrada.")
        return

    receita = receitas_craft[item]

    lote = receita["lote"]
    crafts = math.ceil(quantidade / lote)

    cp = locais_craft.get(receita["local"], "?")

    msg = f"**{item}**\n\n"
    msg += f"Local: {receita['local']} ({cp})\n"
    msg += f"Lote: {lote}\n"
    msg += f"Quantidade pedida: {quantidade}\n"
    msg += f"Crafts necessários: {crafts}\n\n"

    msg += "**Materiais necessários:**\n"

    materiais = receita["materiais"]

    for mat, qtd in materiais.items():
        total = qtd * crafts
        msg += f"{mat} x{total}\n"

    await ctx.send(msg)


bot.run(TOKEN)
