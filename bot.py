import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# WEB SERVER PARA MANTER ONLINE

app = Flask('')

@app.route('/')
def home():
    return "Bot online"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# DISCORD BOT

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

receitas = {

"peca_basica":{
"local":"CP 1053 - Pescadores",
"lote":2,
"materiais":{"ABS":2,"Aluminio":1,"Borracha":1,"Dinheiro":400,"Pedacos_metal":2}
},

"peca_avancada":{
"local":"CP 1053 - Pescadores",
"lote":2,
"materiais":{"Aluminio":1,"Aco":2,"Borracha":1,"Bronze":1,"Dinheiro":600,"Polimero":1}
},

"carregador_pistola":{
"local":"CP 934 - Trevor",
"lote":2,
"materiais":{"Cobre":1,"Niquel":1,"Polvora":1,"Dinheiro":1500}
},

"carregador_smg":{
"local":"CP 934 - Trevor",
"lote":2,
"materiais":{"Cobre":1,"Niquel":2,"Polvora":2,"Dinheiro":2000}
},

"carregador_shotgun":{
"local":"CP 934 - Trevor",
"lote":2,
"materiais":{"Cobre":1,"Niquel":2,"Polvora":2,"Dinheiro":1500}
},

"carregador_rifle":{
"local":"CP 934 - Trevor",
"lote":2,
"materiais":{"Cobre":1,"Niquel":3,"Polvora":3,"Dinheiro":3000}
},

"fibra":{
"local":"CP 3021 - Reciclagem",
"lote":1,
"materiais":{"Couro":2,"Pele":3}
},

"polimero":{
"local":"CP 3021 - Reciclagem",
"lote":1,
"materiais":{"Nylon":1,"Vidro":1}
},

"aluminio":{
"local":"CP 3021 - Reciclagem",
"lote":2,
"materiais":{"Estanho":2,"Tecido":2}
},

"abs":{
"local":"CP 1016 - Laboratorio",
"lote":1,
"materiais":{"Fibra":1,"Plastico":1}
},

"aco":{
"local":"CP 174 - Siderurgia",
"lote":10,
"materiais":{"Mining_drill":1}
},

"bronze":{
"local":"CP 174 - Siderurgia",
"lote":1,
"materiais":{"Cobre":1,"Estanho":1}
},

"barra_ouro":{
"local":"CP 174 - Siderurgia",
"lote":1,
"materiais":[
{"Carvao":6,"Pulseira_ouro":6},
{"Carvao":3,"Ouro_estatal":3}
]
},

"copo_cartao":{
"local":"CP 941 - Craft Geral",
"lote":1,
"materiais":{"Cartao":2}
},

"saco_plastico":{
"local":"CP 941 - Craft Geral",
"lote":5,
"materiais":{"Plastico":1}
},

"tesoura":{
"local":"CP 941 - Craft Geral",
"lote":1,
"materiais":{"Pedacos_metal":5,"Plastico":10}
},

"lata_vazia":{
"local":"CP 941 - Craft Geral",
"lote":1,
"materiais":{"Aluminio":3}
},

"radio":{
"local":"CP 941 - Craft Geral",
"lote":1,
"materiais":{"ABS":5,"Borracha":10,"Restos_eletronicos":10}
},

"rebarbadora":{
"local":"CP 941 - Craft Geral",
"lote":1,
"materiais":{"ABS":20,"Aluminio":40,"Aco":30,"Cobre":8}
},

"lockpick_avancada":{
"local":"CP 941 - Craft Geral",
"lote":1,
"materiais":{"Aco":85,"Parafusos":5}
},

"saco_ginasio":{
"local":"CP 941 - Craft Geral",
"lote":1,
"materiais":{"Tecido":20}
},

"broca_basica":{
"local":"CP 941 - Craft Geral",
"lote":1,
"materiais":{"Aco":90,"Cobre":70,"Pedacos_metal":40}
},

"furadora_basica":{
"local":"CP 941 - Craft Geral",
"lote":1,
"materiais":{"Broca_basica":1,"Mola":10,"Parafusos":10,"Plastico":200,"Restos_eletronicos":100}
},

"fn_1922":{
"local":"Craft armas",
"lote":1,
"materiais":{"Blueprint_pistola":3,"Dinheiro":7500,"Peca_basica":15}
},

"desert_eagle":{
"local":"Craft armas",
"lote":1,
"materiais":{"Blueprint_pistola":10,"Dinheiro":20000,"Peca_basica":50}
},

"colt_scamp":{
"local":"Craft armas",
"lote":1,
"materiais":{"Blueprint_pistola":8,"Dinheiro":20000,"Peca_basica":40}
},

"ranger12":{
"local":"Craft armas",
"lote":1,
"materiais":{"Blueprint_pistola":5,"Dinheiro":6500,"Peca_basica":25}
},

"spas12":{
"local":"Craft armas",
"lote":1,
"materiais":{"Blueprint_rifle":6,"Dinheiro":17000,"Peca_avancada":30}
},

"thompson":{
"local":"Craft armas",
"lote":1,
"materiais":{"Blueprint_smg":6,"Dinheiro":32000,"Peca_avancada":45}
},

"sig_pdw":{
"local":"Craft armas",
"lote":1,
"materiais":{"Blueprint_smg":15,"Dinheiro":45000,"Peca_avancada":75}
},

"akm":{
"local":"Craft armas",
"lote":1,
"materiais":{"Blueprint_rifle":22,"Dinheiro":65000,"Peca_avancada":110}
},

"famas":{
"local":"Craft armas",
"lote":1,
"materiais":{"Blueprint_rifle":24,"Dinheiro":70000,"Peca_avancada":120}
},

"tar21":{
"local":"Craft armas",
"lote":1,
"materiais":{"Blueprint_rifle":24,"Dinheiro":70000,"Peca_avancada":120}
}

}

@bot.command()
async def craft(ctx,item:str,quantidade:int):

    item=item.lower()

    if item not in receitas:
        await ctx.send("Item não encontrado")
        return

    receita=receitas[item]
    lote=receita["lote"]

    if quantidade%lote!=0:
        await ctx.send(f"Quantidade deve ser múltiplo de {lote}")
        return

    crafts=quantidade//lote

    msg=f"Materiais para {quantidade} {item}\n\nLocal: {receita['local']}\n\n"

    materiais=receita["materiais"]

    if isinstance(materiais,list):

        for i,opcao in enumerate(materiais):

            for mat,qtd in opcao.items():
                msg+=f"{mat}: {qtd*crafts}\n"

            if i<len(materiais)-1:
                msg+="\n————— //ou// —————\n\n"

    else:

        for mat,qtd in materiais.items():
            msg+=f"{mat}: {qtd*crafts}\n"

    await ctx.send(msg)

@bot.command()
async def locais(ctx):

    await ctx.send("""
CP 941 - Craft Geral
CP 1016 - Laboratório
CP 174 - Siderurgia
CP 3021 - Reciclagem
CP 934 - Carregadores (Trevor)
CP 1053 - Peças de arma (Pescadores)
""")

@bot.command()
async def receitas(ctx):

    msg="Crafts disponíveis:\n\n"

    for item in receitas:
        msg+=f"!craft {item} quantidade\n"

    await ctx.send(msg)

keep_alive()

bot.run(os.getenv("TOKEN"))
