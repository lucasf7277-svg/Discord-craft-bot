import discord
from discord.ext import commands

TOKEN = "COLOCA_AQUI_O_TOKEN_DO_BOT"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# LOCAIS DE CRAFT

locais = {
"geral":"CP 941 - Craft Geral",
"laboratorio":"CP 1016 - Laboratório",
"siderurgia":"CP 174 - Siderurgia",
"reciclagem":"CP 3021 - Reciclagem",
"carregadores":"CP 934 - Trevor",
"pecas":"CP 1053 - Pescadores",
"armas":"Craft de armas"
}

# RECEITAS

receitas = {

"peca_basica":{
"local":"pecas",
"lote":2,
"materiais":{"ABS":2,"Aluminio":1,"Borracha":1,"Dinheiro":400,"Pedaco_metal":2}
},

"peca_avancada":{
"local":"pecas",
"lote":2,
"materiais":{"Aluminio":1,"Aco":2,"Borracha":1,"Bronze":1,"Dinheiro":600,"Polimero":1}
},

"carregador_pistola":{
"local":"carregadores",
"lote":2,
"materiais":{"Cobre":1,"Niquel":1,"Polvora":1,"Dinheiro":1500}
},

"carregador_smg":{
"local":"carregadores",
"lote":2,
"materiais":{"Cobre":1,"Niquel":2,"Polvora":2,"Dinheiro":2000}
},

"carregador_shotgun":{
"local":"carregadores",
"lote":2,
"materiais":{"Cobre":1,"Niquel":2,"Polvora":2,"Dinheiro":1500}
},

"carregador_rifle":{
"local":"carregadores",
"lote":2,
"materiais":{"Cobre":1,"Niquel":3,"Polvora":3,"Dinheiro":3000}
},

"fibra":{
"local":"reciclagem",
"lote":1,
"materiais":{"Couro":2,"Pele":3}
},

"polimero":{
"local":"reciclagem",
"lote":1,
"materiais":{"Nylon":1,"Vidro":1}
},

"aluminio":{
"local":"reciclagem",
"lote":2,
"materiais":{"Estanho":2,"Tecido":2}
},

"abs":{
"local":"laboratorio",
"lote":1,
"materiais":{"Fibra":1,"Plastico":1}
},

"aco":{
"local":"siderurgia",
"lote":10,
"materiais":{"Mining_drill":1}
},

"bronze":{
"local":"siderurgia",
"lote":1,
"materiais":{"Cobre":1,"Estanho":1}
},

"barra_ouro":{
"local":"siderurgia",
"lote":1,
"materiais":[
{"Carvao":6,"Pulseira_ouro":6},
{"Carvao":3,"Ouro_estatal":3}
]
},

"copo_cartao":{
"local":"geral",
"lote":1,
"materiais":{"Cartao":2}
},

"saco_plastico":{
"local":"geral",
"lote":5,
"materiais":{"Plastico":1}
},

"tesoura":{
"local":"geral",
"lote":1,
"materiais":{"Pedaco_metal":5,"Plastico":10}
},

"lata_vazia":{
"local":"geral",
"lote":1,
"materiais":{"Aluminio":3}
},

"radio":{
"local":"geral",
"lote":1,
"materiais":{"ABS":5,"Borracha":10,"Restos_eletronicos":10}
},

"rebarbadora":{
"local":"geral",
"lote":1,
"materiais":{"ABS":20,"Aluminio":40,"Aco":30,"Cobre":8}
},

"lockpick_avancada":{
"local":"geral",
"lote":1,
"materiais":{"Aco":85,"Parafusos":5}
},

"saco_ginasio":{
"local":"geral",
"lote":1,
"materiais":{"Tecido":20}
}

}

# COMANDO CRAFT

@bot.command()
async def craft(ctx,item:str,quantidade:int):

    item=item.lower()

    if item not in receitas:
        await ctx.send("Item não encontrado.")
        return

    receita=receitas[item]
    lote=receita["lote"]

    if quantidade%lote!=0:
        await ctx.send(f"A quantidade deve ser múltiplo de {lote}")
        return

    crafts=quantidade//lote

    mensagem=f"**Craft de {quantidade} {item}**\n"
    mensagem+=f"Local: {locais[receita['local']]}\n\n"

    materiais=receita["materiais"]

    if isinstance(materiais,list):

        for i,opcao in enumerate(materiais):

            for mat,qtd in opcao.items():
                mensagem+=f"{mat}: {qtd*crafts}\n"

            if i<len(materiais)-1:
                mensagem+="\n------ //ou// ------\n\n"

    else:

        for mat,qtd in materiais.items():
            mensagem+=f"{mat}: {qtd*crafts}\n"

    await ctx.send(mensagem)

# COMANDO RECEITAS

@bot.command()
async def receitas(ctx):

    texto="**Receitas disponíveis:**\n\n"

    for item in receitas:
        texto+=f"!craft {item} quantidade\n"

    await ctx.send(texto)

# COMANDO LOCAIS

@bot.command()
async def locais(ctx):

    texto="**Locais de craft:**\n\n"

    for nome,cp in locais.items():
        texto+=f"{nome} → {cp}\n"

    await ctx.send(texto)

@bot.event
async def on_ready():
    print(f"Bot ligado como {bot.user}")

bot.run(TOKEN)
