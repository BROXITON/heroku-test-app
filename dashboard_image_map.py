import dash
import dash_html_components as html

app = dash.Dash()

filename = app.get_asset_url('dashboard.gif')

app.layout = html.Div([ 
		html.MapEl([
			html.Area(target='' ,alt='gerar resultados expressivos aos acionistas' ,title='gerar resultados expressivos aos acionistas' ,href='http://www.google.com' ,coords='427,136,319,89' ,shape='rect'),
			html.Area(target='' ,alt='otimizar continuamente a estrutura de custos' ,title='otimizar continuamente a estrutura de custos' ,href='http://www.yahoo.com' ,coords='142,170,34,123' ,shape='rect'),
			html.Area(target='' ,alt='assegurar a realizacao dos investimentos' ,title='assegurar a realizacao dos investimentos' ,href='http://www.oracle.com' ,coords='283,170,173,120' ,shape='rect'),
			html.Area(target='' ,alt='maximizar as receitas' ,title='maximizar as receitas' ,href='4' ,coords='575,169,464,123' ,shape='rect'),
			html.Area(target='' ,alt='ser um agente de desenvolvimento regional' ,title='ser um agente de desenvolvimento regional' ,href='5' ,coords='650,125,757,172' ,shape='rect'),
			html.Area(target='' ,alt='ser referenciado no mercado pela qualidade de servicos' ,title='ser referenciado no mercado pela qualidade de servicos' ,href='6' ,coords='307,184,433,232' ,shape='rect'),
			html.Area(target='' ,alt='garantir a satisfacao do poder concedente' ,title='garantir a satisfacao do poder concedente' ,href='7' ,coords='115,247,223,294' ,shape='rect'),
			html.Area(target='' ,alt='promover a satisfacao do usuario' ,title='promover a satisfacao do usuario' ,href='8' ,coords='316,250,425,290' ,shape='rect'),
			html.Area(target='' ,alt='ter marca e imagem de credibilidade' ,title='ter marca e imagem de credibilidade' ,href='9' ,coords='504,245,612,293' ,shape='rect'),
			html.Area(target='' ,alt='gerir operacao viaria e pedagiada com eficiencia' ,title='gerir operacao viaria e pedagiada com eficiencia' ,href='10' ,coords='212,356,319,403' ,shape='rect'),
			html.Area(target='' ,alt='otimizar a manutencao viaria e implantacao de projetos' ,title='otimizar a manutencao viaria e implantacao de projetos' ,href='11' ,coords='339,355,446,403' ,shape='rect'),
			html.Area(target='' ,alt='executar uma gestao eficaz do contrato de concessao' ,title='executar uma gestao eficaz do contrato de concessao' ,href='12' ,coords='210,411,318,461' ,shape='rect'),
			html.Area(target='' ,alt='realizar a gestao eficaz das compras e contratacoes' ,title='realizar a gestao eficaz das compras e contratacoes' ,href='13' ,coords='338,411,447,461' ,shape='rect'),
			html.Area(target='' ,alt='fortalecer os relacionamentos com as partes interessadas' ,title='fortalecer os relacionamentos com as partes interessadas' ,href='14' ,coords='503,340,613,388' ,shape='rect'),
			html.Area(target='' ,alt='atrair trafego no curto medio e longo prazos' ,title='atrair trafego no curto medio e longo prazos' ,href='15' ,coords='653,359,758,407' ,shape='rect'),
			html.Area(target='' ,alt='identificar e desenvolver novos negocios' ,title='identificar e desenvolver novos negocios' ,href='16' ,coords='652,416,759,462' ,shape='rect'),
			html.Area(target='' ,alt='aprimorar os processos de gestao e a governanca corporativa' ,title='aprimorar os processos de gestao e a governanca corporativa' ,href='17' ,coords='20,512,127,560' ,shape='rect'),
			html.Area(target='' ,alt='melhorar comunicacao interna e a integracao entre as areas' ,title='melhorar comunicacao interna e a integracao entre as areas' ,href='18' ,coords='130,514,251,563' ,shape='rect'),
			html.Area(target='' ,alt='fomentar a inovacao em busca de novas solucoes' ,title='fomentar a inovacao em busca de novas solucoes' ,href='19' ,coords='256,514,348,561' ,shape='rect'),
			html.Area(target='' ,alt='atrair talentos, desenvolver, reter e promover sucessao' ,title='atrair talentos, desenvolver, reter e promover sucessao' ,href='20' ,coords='371,511,485,562' ,shape='rect'),
			html.Area(target='' ,alt='proporcionar condicoes de seguranca para colaboradores, terceiros e usuarios' ,title='proporcionar condicoes de seguranca para colaboradores, terceiros e usuarios' ,href='21' ,coords='513,511,644,559' ,shape='rect'),
			html.Area(target='' ,alt='promover acoes de responsabilidade socioambiental' ,title='promover acoes de responsabilidade socioambiental' ,href='22' ,coords='651,513,764,562' ,shape='rect'),
			html.Area(target='' ,alt='resultados' ,title='resultados' ,href='23' ,coords='76,101,7,88' ,shape='rect'),
			html.Area(target='' ,alt='desenvolvimento regional' ,title='desenvolvimento regional' ,href='24' ,coords='621,89,775,99' ,shape='rect'),
			html.Area(target='' ,alt='clientes' ,title='clientes' ,href='25' ,coords='9,187,62,199' ,shape='rect'),
			html.Area(target='' ,alt='processos internos' ,title='processos internos' ,href='26' ,coords='8,340,65,366' ,shape='rect'),
			html.Area(target='' ,alt='aprendizado e crescimento' ,title='aprendizado e crescimento' ,href='27' ,coords='6,490,168,499' ,shape='rect'),
			html.Area(target='' ,alt='eficiencia operacional' ,title='eficiencia operacional' ,href='28' ,coords='196,336,313,346' ,shape='rect'),
			html.Area(target='' ,alt='tecnologia e organizacao' ,title='tecnologia e organizacao' ,href='29' ,coords='204,491,335,502' ,shape='rect'),
			html.Area(target='' ,alt='pessoas' ,title='pessoas' ,href='30' ,coords='435,493,478,501' ,shape='rect'),
			html.Area(target='' ,alt='seguranca e responsabilidade' ,title='seguranca e responsabilidade' ,href='31' ,coords='607,491,764,501' ,shape='rect'),
			html.Area(target='' ,alt='crescimento' ,title='crescimento' ,href='32' ,coords='648,337,717,346' ,shape='rect')
		],
		name='map'), html.Img(src=filename, useMap='#map')
],margin='auto')  


if __name__ == '__main__':

    app.run_server(debug=True)
