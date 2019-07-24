import discord, asyncio, m_log, m_version

bot_ver = "2.0.0-t01"

def help(params):
    try:
        if params[0] == '일상':
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
        elif params[0] == '게임':
            try:
                if params[1] == '섯다':
                    text = "명령어 : 루냥아 섯다 (숫자1) (숫자2), "
                    text+= "0~9까지의 숫자 두개를 입력해 진행합니다"
                    embed=discord.Embed(title="두장섯다 사용 방법", description=text, color=0xffff00)
                    text = "땡 > 삥 > 끗"
                    embed.add_field(name="족보 순위", value=text, inline=False)
                    text = "두 패가 같은 경우 (장땡 ~ 삥땡)"
                    embed.add_field(name="땡", value=text, inline=False)
                    text = "알리(1+2), 독사(1+4), 구삥(1+9), 장삥(1+10), "
                    text+= "장사(4+10), 세륙(4+6)"
                    embed.add_field(name="삥", value=text, inline=False)
                    text = "두 패 합의 일의 자리 숫자 (갑오 ~ 망통)"
                    embed.add_field(name="끗", value=text, inline=False)
                elif params[1] == '제비뽑기':
                    text = "명령어 : 루냥아 제비뽑기 (선택지1) (선택지2) ... , (결과1) (결과2) ..."
                    embed=discord.Embed(title="제비뽑기 사용 방법", description=text, color=0xffff00)
                    text = "각 항목은 띄어쓰기로 구분, 선택지와 결과는 쉼표(,)로 구분!"
                    embed.add_field(name="사용 방법", value=text, inline=False)
                    text = "선택지와 결과의 개수는 동일해야 합니다"
                    embed.add_field(name="주의사항", value=text, inline=True)
                elif params[1] == '주사위':
                    text = "명령어 : 루냥아 주사위"
                    embed=discord.Embed(title="주사위 사용 방법", description=text, color=0xffff00)
            except IndexError:
                embed=discord.Embed(title="도움말", description="게임", color=0xffff00)
                embed.set_author(name="게임 사용 방법 보기 : 루냥아 도와줘 게임 (게임이름)")
                text = "CPU와 두장섯다를 진행합니다"
                embed.add_field(name="섯다", value=text, inline=False)
                text = "CPU가 제비뽑기를 실행합니다"
                embed.add_field(name="제비뽑기", value=text, inline=False)
                text = "1부터 6까지 무작위의 숫자를 출력합니다"
                embed.add_field(name="루냥아 주사위", value=text, inline=False)
        elif params[0] == '유용한 기능':
                embed=discord.Embed(title="도움말", description="유용한 기능", color=0x00ff00)
                text = "Wolfram|Alpha 계산 쿼리를 제공합니다"
                embed.add_field(name="루냥아 계산해줘 (계산식)", value=text, inline=False)
                text = "Wolfram|Alpha 플롯 계산 쿼리를 제공합니다(실험적인 기능입니다!)"
                embed.add_field(name="루냥아 계산해줘 이미지 (계산식)", value=text, inline=False)
                text = "어느것을 고를까요 알아맞춰 봅시다"
                embed.add_field(name="루냥아 골라줘 (선택지1) (선택지2) ...", value=text, inline=False)
                text = "루냥이가 대신 말해줍니다 (혐오 단어가 감지되는 경우 거부됩니다)"
                embed.add_field(name="루냥아 확성기 (할 말)", value=text, inline=False)
    except IndexError:
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
        embed.set_footer(text="Copyright (C) 2017 - 2019 libertin | v" + m_version.bot_ver)
    return embed

def updatelog():
    updlog = "test"
    return updlog
