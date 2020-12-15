color_number = 8

color_picked = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
            for i in range(number_of_colors)]

await ctx.send(embed=discord.Embed(
            color=color_picked 
            description = "Random color: " + color_picked
)
