# Define a função para desenhar o mapa mental de forma mais organizada
def draw_mind_map():
    plt.figure(figsize=(20, 20))
    
    # Definir a posição dos nós de forma radial
    pos = {
        'Embriologia': (0.5, 0.9),
        'Disco Embrionário': (0.2, 0.75),
        'Bilaminar': (0.1, 0.7),
        'Trilaminar': (0.3, 0.7),
        'Gastrulação': (0.5, 0.75),
        'Linha Primitiva': (0.4, 0.7),
        'Nó Primitivo': (0.5, 0.7),
        'Epiblastos': (0.6, 0.7),
        'Formação dos Três Folhetos': (0.5, 0.65),
        'Ectoderma': (0.4, 0.6),
        'Neuroectoderma': (0.35, 0.55),
        'Crista Neural': (0.45, 0.55),
        'Placa Neural': (0.4, 0.5),
        'Mesoderma': (0.5, 0.6),
        'Somitos': (0.45, 0.55),
        'Mesoderma Lateral': (0.55, 0.55),
        'Somatopleura': (0.5, 0.5),
        'Esplacnopleura': (0.6, 0.5),
        'Mesoderma Intermediário': (0.5, 0.55),
        'Mesoderma Paraxial': (0.5, 0.5),
        'Miótomo': (0.45, 0.45),
        'Esclerótomo': (0.5, 0.45),
        'Dermótomo': (0.55, 0.45),
        'Endoderma': (0.6, 0.6),
        'Formação do Sistema Nervoso': (0.8, 0.75),
        'Tubo Neural': (0.75, 0.7),
        'Encéfalo': (0.85, 0.7),
        'Prosencéfalo': (0.8, 0.65),
        'Mesencéfalo': (0.85, 0.65),
        'Romboencéfalo': (0.9, 0.65),
        'Medula Espinhal': (0.8, 0.7),
        'Notocorda e Eixos Corporais': (0.2, 0.55),
        'Notocorda': (0.15, 0.5),
        'Eixos Antero-Posterior, Dorso-Ventral, Sinistro-Dextro': (0.25, 0.5),
        'Morfógenos e Sinalização': (0.5, 0.5),
        'BMP4': (0.45, 0.45),
        'Noggin': (0.5, 0.45),
        'Cordin': (0.55, 0.45),
        'FGF': (0.5, 0.4),
        'WNT': (0.45, 0.4),
        'SHH': (0.55, 0.4),
        'Desenvolvimento de Órgãos e Sistemas': (0.5, 0.4),
        'Sistema Digestório': (0.45, 0.35),
        'Sistema Urinário': (0.5, 0.35),
        'Sistema Cardiovascular': (0.55, 0.35),
        'Coração': (0.5, 0.3),
        'Aortas': (0.55, 0.3),
    }
    
    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(15, 15))
    
    # Desenhar nós
    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue', alpha=0.9, ax=ax)
    
    # Desenhar arestas
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrows=True, ax=ax)
    
    # Desenhar rótulos
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black', font_weight='bold', ax=ax)
    
    # Ocultar eixos
    ax.axis('off')
    
    # Adicionar título
    plt.title('Mapa Mental de Embriologia', fontsize=20)
    
    # Salvar a imagem
    plt.savefig('/mnt/data/Mapa_Mental_Embriologia_Organizado_2.png', format='PNG')
    plt.show()

draw_mind_map()
