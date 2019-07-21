import discord, asyncio, m_log, main

def help(arg):
    if arg[0] == '':
        text = "[민원창구](https://discordapp.com/invite/yyS9x5V) "
        text+= "[봇 초대하기](https://discordapp.com/oauth2/authorize?client_id=598080777565241354&scope=bot&permissions=388160)"
        embed=discord.Embed(title="기계식 루냥이를 초대해주셔서 감사합니다!", description=text, color=0xff0080)
        embed.set_author(name="기계식 루냥이 사용 방법",icon_url=client.user.avatar_url)
        text = "루냥아 도와줘 (항목), 루냥아 업데이트내역"
        embed.add_field(name="도움말", value=text, inline=False)
        text = "루냥아 배고파, 루냥이 귀여워, 루냥이 쓰담쓰담, "
        text+= "루냥아 짖어봐, 루냥아 손, 와! 샌즈!"
        embed.add_field(name="일상", value=text, inline=False)
        text = "루냥아 섯다, 루냥아 제비뽑기, 루냥아 주사위"
        embed.add_field(name="게임", value=text, inline=False)
        text = "루냥아 계산해줘 (계산식), 루냥아 계산해줘 이미지 (계산식), "
        text+= "루냥아 확성기, 루냥아 골라줘"
        embed.add_field(name="유용한 기능", value=text, inline=False)
        embed.set_footer(text="Copyright (C) 2017 - 2019 libertin | v" + main.bot_ver)
    elif arg[0] == '일상':
        embed=discord.Embed(title="도움말", description="일상 항목", color=0x8080ff)
        text = "랜덤으로 음식을 추천해줍니다 (음식을 사주지는 않습니다!)"
        embed.add_field(name="루냥아 배고파", value=text, inline=False)
        text = "자기 자신을 귀여워합니다 "
        text+= "(루냥이 커여워, 귀냥이 루여워, 커냥이 루여워 도 가능합니다)"
        embed.add_field(name="루냥이 귀여워", value=text, inline=False)
        text = "자기 자신한테 사이버(?) 쓰다듬을 선물해줍니다"
        embed.add_field(name="루냥이 쓰담쓰담", value=text, inline=False)
        text = "(대충 짖는 소리)"
        embed.add_field(name="루냥아 짖어봐", value=text, inline=False)
        text = "(대충 손 내밀기)"
        embed.add_field(name="루냥아 손", value=text, inline=False)
        text = "언더테일 아시는구나!"
        embed.add_field(name="와! 샌즈!", value=text, inline=False)
    elif arg[0] == '게임':
        if arg[1] == None:
            
        elif arg[1] == '섯다':
            
        elif arg[1] == '제비뽑기':
            
        elif arg[1] == '주사위':
            
        else:
            
    elif arg[0] == '유용한 기능':
    return embed
