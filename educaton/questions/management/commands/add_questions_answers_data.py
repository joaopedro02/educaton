from django.core.management.base import BaseCommand, CommandError

from questions.models import Question, Answers


class Command(BaseCommand):
    help="add data to app data bank"
    
    def handle(self,*args,**options):
        
        vet = [
            "Tenho fama de dizer o que penso claramente e sem rodeios.",
            "A maior parte das vezes, sinto-me seguro(a) do que está correto e do que está incorreto.",
            "Muitas vezes, tomo atitudes sem olhar às consequências.",
            "Normalmente, procuro resolver os problemas metodicamente, passo a passo.",
            "Creio que o formalismo restringe e limita a atuação livre das pessoas.",
            "Interessa-me saber quais são os critérios e valores das pessoas",
            "Penso que agir intuitivamente pode ser sempre tão válido como agir reflexivamente.",
            "Creio que o mais importante é que as coisas funcionem, , independentemente, dos métodos.",
            "Estou atento a todos os pormenores das disciplinas que frequento (resumos, textos, etc).",
            "Agrada-me ter tempo para preparar os meus trabalhos com consciência.",
            "Sou adepto(a) da autodisciplina, seguindo uma certa ordem, por exemplo, no no estudo e no exercício físico.",
            "Quando ouço uma ideia nova, começo logo a pensar como poderei colocá-la em prática.",
            "Prefiro ideias originais e inovadoras, ainda que não sejam práticas.",
            "Só admito e me adapto às normas, se elas servem para que eu atinja os meus objetivos.",
            "Adapto-me melhor às pessoas reflexivas, do que àquelas demasiado espontâneas e imprevisíveis.",
            "Escuto com mais frequência do que falo.",
            "Prefiro as coisas estruturadas às desordenadas.",
            "Preocupo-me em interpretar, cuidadosamente, a informação disponível antes de tirar uma conclusão.",
            "Antes de fazer alguma coisa, analiso com cuidado as suas vantagens e inconvenientes.",
            "Estimula-me o fato de fazer algo novo e diferente.",
            "Procuro, quase sempre, ser coerente com os meus princípios, seguindo critérios e sistemas de valores.",
            "Quando há uma discussão, não gosto de rodeios.",
            "Tenho tendência a relacionar-me de um modo distante, e algo formal com as pessoas com quem trabalho ou estudo.",
            "Gosto mais das pessoas realistas e concretas, do que das idealistas.",
            "Tenho dificuldade em ser criativo(a) e em romper com as estruturas existentes.",
            "Sinto-me bem com pessoas espontâneas.",
            "Quase sempre expresso abertamente os meus sentimentos.",
            "Gosto de analisar as coisas por todos os ângulos.",
            "Incomoda-me ver que as pessoas não levam as coisas a sério.",
            "Sinto-me atraído(a) a experimentar e praticar as últimas técnicas e novidades.",
            "Sou cauteloso(a) na hora de tirar conclusões.",
            "Prefiro contar com o maior número de fontes de informação, ou seja, quantos mais dados tiver, melhor.",
            "Tenho a tendência de ser perfeccionista.",
            "Prefiro ouvir as opiniões dos outros antes de expor as minhas.",
            "Gosto de enfrentar a vida de forma espontânea, sem ter que planejar tudo previamente.",
            "Nas discussões, gosto de observar como agem os outros participantes.",
            "Sinto-me pouco à vontade, com pessoas demasiado críticas e minuciosas.",
            "Avalio as ideias dos outros pelo seu valor prático, frequentemente.",
            "Sinto-me oprimido(a ), se me obrigam a acelerar o trabalho para cumprir um prazo.",
            "Apoio as ideias práticas e realistas em reuniões.",
            "É melhor aproveitar o momento presente, do que viver pensando no passado ou no futuro.",
            "As pessoas que desejam sempre apressar as coisas me incomodam.",
            "Nos grupos de discussão emito ideias novas e espontâneas.",
            "Penso que são mais consistentes as decisões fundamentadas numa análise minuciosa do que as baseadas na intuição.",
            "Detecto a inconsistência e os pontos frágeis nas argumentações dos outros com frequência.",
            "Creio que desobedeço às regras com mais frequência do que as sigo.",
            "Percebo, com frequência, formas melhores e mais práticas de fazer as coisas.",
            "Geralmente, falo mais do que escuto.",
            "Prefiro distanciar-me dos fatos e observá-los com outras perspectivas.",
            "Estou convencido(a) de que a lógica e a razão devem imperar .",
            "Gosto de buscar novas experiências.",
            "Quando ouço uma ideia ou uma nova abordagem, tento imediatamente encontrar aplicações concretas.",
            "Penso que devemos chegar, o mais rapidamente possível, à ideia central dos assuntos.",
            "Esforço-me sempre para tirar conclusões e ideias claras.",
            "Prefiro discutir questões concretas, e não perder tempo com ideias abstratas.",
            "Fico impaciente quando ouço explicações irrelevantes ou incoerentes.",
            "Verifico sempre, com antecedência, se as coisas funcionam realmente.",
            "Faço vários rascunhos antes da redação definitiva de um trabalho.",
            "Nas discussões tenho consciência que ajudo a manter os outros centrados no tema, evitando divagações.",
            "Observo com frequência, que sou uma das pessoas mais objetivas e ponderadas nas discussões.",
            "Quando algo corre mal, tento logo fazer melhor.",
            "Rejeito ideias originais se me parecerem impraticáveis.",
            "Antes de tomar uma decisão, pondero sempre diversas alternativas.",
            "Eu tento prever o futuro com frequência.",
            "Nos debates e discussões prefiro desempenhar um papel secundário em vez de ser o(a) líder ou o(a) que mais participa.",
            "As pessoas que não agem com lógica me incomodam.",
            "Incomoda-me ter que planejar e prever as coisas.",
            "Penso que muitas vezes os fins justificam os meios.",
            "Costumo pensar sobre os assuntos e problemas com profundidade.",
            "O trabalhar consciente enche-me de satisfação e orgulho",
            "Tento descobrir os princípios e as teorias que fundamentam os acontecimentos.",
            "Sou capaz de ferir os sentimentos de outros para atingir os meus objetivos.",
            "Não me importo de fazer tudo o que for necessário para que o meu trabalho seja eficiente.",
            "Sou umas das pessoas que mais animam as festas, com frequência.",
            "Aborreço-me com o trabalho metódico e minucioso, rapidamente.",
            "As pessoas costumam pensar que sou insensível aos seus sentimentos.",
            "Costumo agir pela minha intuição.",
            "Se faço parte de um grupo de trabalho, procuro que seja seguido um plano ou uma metodologia.",
            "Com frequência tenho interesse em descobrir o que pensam as pessoas.",
            "Evito os assuntos subjetivos, ambíguos e pouco claros.",
        ]
        
        vet1 = [
            "Livros são muito importantes para mim.",
            "Gosto de ouvir as palavras na minha cabeça antes falar ou escrevêlas.",
            "Aproveito mais ouvindo rádio ou ubooks do que vendo televisão ou filmes.,
            "Gosto de jogos que envolvam palavras, como por exemplo: palavras cruzadas, anagramas ou scrabble.",
            "Gosto de me divertir ou a outros com palavras difíceis de se pronunciar, rimas sem sentido ou palavras homônimas e homógrafas.",
            "Por vezes tenho que parar o que estou dizendo para repetir ou explicar o significado das palavras que falo ou que escrevo.",
            "Na escola sempre considerei Português, Estudos Sociais e História mais fáceis do que Matemática e Ciências.",
            "Quando estou dirigindo numa estrada, presto mais atenção nas palavras escritas nas placas do que na paisagem.",
            "Frequentemente minhas conversas incluem referências de assuntos que leio ou ouço.",
            "Recentemente escrevi algo de que me orgulhei bastante, ou que me rendeu o reconhecimento de outras pessoas.",
            "Consigo facilmente computar números de cabeça.",
            "Matemática e/ou ciência estavam entre minhas matérias prediletas na escola.",
            "Gosto de brincar com jogos ou resolver quebracabeças que exijam raciocínio lógico, como o Sudoku.",
            "Gosto de fazer pequenas experiências do tipo “e se...” (Por exemplo: “E se eu dobrasse a quantidade de água usada neste experimento?”).",
            "Minha mente busca padrões, regularidades ou sequências lógicas nas coisas.",
            "Tenho muito interesse em inovações na área da ciência.",
            "Penso que quase tudo tem uma explicação racional.",
            "Às vezes penso em conceitos abstratos, sem palavras e sem imagens.",
            "Gosto de achar coisas que não têm lógica no que as pessoas dizem e fazem em casa ou no trabalho.",
            "Sintome mais seguro(a) quando algo já foi medido, categorizado, analisado ou de algum modo quantificado.",
            "Frequentemente vejo imagens visuais claras quando fecho meus olhos.",
            "Sou sensível às cores.",
            "Frequentemente uso câmera fotográfica ou de vídeo para registrar o que vejo ao meu redor.",
            "Gosto de brincar com jogos de quebracabeça, labirintos e outros jogos visuais.",
            "Quando durmo tenho sonhos muito vivos.",
            "Geralmente consigo me virar num território que me é desconhecido.",
            "Gosto de desenhar ou rabiscar.",
            "Na escola, Geometria foi mais fácil para mim do Álgebra.",
            "Consigo imaginar como seria a aparência de uma coisa vista por cima, como se fosse vista por um um pássaro.",
            "Prefiro material de leitura que tenha muitas ilustrações.",
            "As pessoas me procuram para ouvir conselho e orientação no trabalho, faculdade ou em minha vizinhança.",
            "Prefiro esportes coletivos, como voleibol ou basquetebol, do que esportes individuais como natação e corrida.",
            "Quando tenho um problema, me sinto mais inclinado a procurar alguém para me ajudar do que tentar resolvêlo por mim mesmo.",
            "Tenho pelo menos três pessoas em que confio ou com as quais me dou bem.",
            "Prefiro passatempos em grupo, como Banco Imobiliário ou Bridge, do que recreações individuais como vídeos ou filmes.",
            "Gosto do desafio de ensinar o que sei fazer a uma ou a um grupo de pessoas.",
            "Eu me considero líder, ou algumas pessoas me chamam de líder.",
            "Eu me sinto bem no meio de muitas pessoas.",
            "Gosto de me envolver em atividades sociais que estejam relacionadas ao meu trabalho, igreja ou comunidade.",
            "Eu prefiro passar minhas noites em festas agitadas do que ficar sozinho dentro de casa.",
            "Estou envolvido(a) regularmente em pelo menos um esporte ou atividade física.",
            "Acho difícil ficar parado por muito tempo.",
            "Gosto de trabalhar manualmente em atividades concretas tais como costura, tecelagem,escultura em madeira, carpintaria/marcenaria, ou modelagem.",
            "Geralmente minhas melhores ideias aparecem quando saio para um longo passeio ou corrida, ou quando me envolvo com algum tipo de atividade física.",
            "Frequentemente gosto de passar o tempo ocioso que tenho ao ar livre.",
            "Frequentemente faço gestos com as mãos ou outras formas de linguagem corporal quando estou conversando com alguém.",
            "Eu tenho necessidade de tocar nas coisas para aprender mais a respeito delas.",
            "Em parque de diversões, gosto de andar em trem fantasma, montanha russa ou de ter experiências físicas emocionantes.",
            "Eu me descreveria como uma pessoa que tem boa coordenação física.",
            "Tenho necessidade de praticar uma nova habilidade em vez de simplesmente ler sobre ela, ou assistir a um vídeo que a descreva.",
            "Tenho um voz agradável para canto.",
            "Consigo identificar um nota musical desafinada.",
            "Frequentemente ouço música pelo rádio, smartphone, etc.",
            "Eu toco um instrumento musical.",
            "Não imagino minha vida sem música.",
            "Às vezes estou cantarolando ou me surpreendo com alguma melodia passando pela cabeça.",
            "Facilmente consigo acompanhar o ritmo de uma música com um simples instrumento de percussão.",
            "Conheço a melodia de muitas canções ou peças musicais.",
            "Após ouvir uma música poucas vezes, normalmente sou capaz de cantála de modo razoavelmente preciso.",
            "Frequentemente batuco uns sons ou cantarolo pequenas melodias, enquanto estou trabalhando, estudando ou aprendendo algo novo.",
            "Regularmente fico um tempo sozinho para meditar, refletir ou pensar sobre questões importantes da vida.",
            "Gosto de atividades ou questionários que permitam conhecerme melhor.",
            "Sou capaz de reagir aos contratempos da vida com tranquilidade.",
            "Tenho um hobby especial ou um interesse que conservo só para mim.",
            "Penso regularmente em algumas metas importantes que tenho para a minha vida.",
            "Tenho uma visão realista de minhas potencialidades e fraquezas (como resultado do que me dizem as pessoas ou recebo de outras fontes).",
            "Eu prefiro passar o tempo sozinho numa cabana do que num clube de campo cheio de pessoas em volta.",
            "Eu me considero uma pessoa com força de vontade, ou de maneira independente de pensar.",
            "Tenho um diário pessoal onde escrevo regularmente.",
            "Eu já trabalho como autônomo ou tenho pensado seriamente em começar meu próprio negócio.",
            "Gosto de atividades em contato com a natureza, como acampar ou andar.",
            "Preocupome e contribuo com a preservação do meio ambiente.",
            "Adoro animais e tenho (ou gostaria de ter) um em casa.",
            "Tento passar o máximo de tempo possível fora de casa.",
            "Tenho interesse em descobrir e aprender coisas relacionadas com a natureza.",
            "Gosto de livros e reportagens sobre a natureza.",
            "Gosto de visitar zoológicos ou aquários.",
            "Prefiro passar as férias acampando, do que em um complexo turístico.",
            "Gosto de participar de projetos de preservação do meio ambiente.",
            "Gosto muito de flores e jardins.",
        ]
       

        for questao in vet:
            q = Question(question_text = questao, form = 1)
            q.save()
            q.answers_set.create(answers_text="0",answers_value=0)
            q.answers_set.create(answers_text="1",answers_value=1)
            q.answers_set.create(answers_text="2",answers_value=2)
            q.answers_set.create(answers_text="3",answers_value=3)
            
        for questao in vet1:
            q = Question(question_text = questao, form = 2)
            q.save()
            q.answers_set.create(answers_text="0",answers_value=0)
            q.answers_set.create(answers_text="1",answers_value=1)
            q.answers_set.create(answers_text="2",answers_value=2)
            q.answers_set.create(answers_text="3",answers_value=3)
            
       
        
