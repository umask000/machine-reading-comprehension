# -*- coding: utf-8 -*-
# @author: caoyang
# @email: caoyang@163.sufe.edu.cn

import json
from pprint import pprint

from setting import *

def race():

    for filename in os.listdir(os.path.join(DATASET_DIR, 'RACE', 'train', 'high')):

        with open(os.path.join(DATASET_DIR, 'RACE', 'train', 'high', filename), 'r') as f:

            data = json.load(f)
            pprint(data)




"""{'answers': ['C', 'B', 'B', 'A', 'D'],
 'article': 'Surfing the net when you should be finishing a work report, '
            'changing clothes when you have a train to catch, or perhaps even '
            "lying in bed when you've promised yourself you'll work out. Sound "
            "familiar? You aren't alone. We all procrastinate   sometimes, "
            "especially when it comes to things we aren't really fond of. And "
            'while the number of activities we delay doing in any given week '
            "varies from person to person, it's fair to say that none of us is "
            'super-efficient 100 percent of the time.\n'
            'A study revealed that we spend about 218 minutes procrastinating '
            'every day, which amounts to 55 days of lost time each year. We '
            'might not think these figures particularly worthy of worry, but '
            'when we look at the overall impact of procrastination on our '
            'lives, _ Not only does this cost financial loss, it also affects '
            "peace of mind. And procrastination isn't just a money thief ---- "
            'it steals time too. In general, people who continually put things '
            'off are unhappier, as well as being less wealthy and healthy.\n'
            'So why do we do it? "When we avoid taking action, we\'re really '
            'avoiding pain," explains psychiatrist   Phil Stutz. For most of '
            "us, pain avoidance isn't limited to one situation. It applies to "
            "almost anything that's painful. Most of us try our best never to "
            "leave a comfort zone. That's why we sacrifice something much more "
            'valuable: time. "Our time on earth is limited," Stutz adds. '
            '"Every moment is an opportunity we\'ll never have again. '
            'Procrastinators act as if they have all the time in the world. '
            "But deep down, they know they're wasting parts of their life. The "
            'trouble is, most of them don\'t know how to free themselves."\n'
            'One way he says we can reach this level of freedom is by '
            'overcoming the pain of avoidance using daily visualization  . '
            '"Picture the pain you\'re avoiding as a black cloud in front of '
            'you," Stutz says. "Notice how you\'re fed up with the ways this '
            "pain has held you back in life, and tell yourself that you're "
            "determined to conquer it. Then it's time to get through the cloud "
            'and to the other side -- where you\'re free." It is obvious that '
            'this tool works when we want to procrastinate. We then get into '
            'the habit of moving "towards" pain instead of away from it.\n'
            'In addition to the fact that procrastinators suffer more health '
            'problems, procrastination also destroysteamwork and personal '
            'relationships because it shifts the burden of responsibilities '
            'onto others. So next time you think about putting something off, '
            'remember the impact it will have. Experts insist: procrastinators '
            'can change their behavior, it takes a lot of self-work but in the '
            "end, it's worth the effort. And start today, not tomorrow.",
 'id': 'high9999.txt',
 'options': [['presenting abnormal things',
              'asking related questions',
              'mentioning habitual activities',
              'comparing different opinions'],
             ['leads to different results for different persons',
              "is likely to have bad effects on people's life",
              'may not be particularly worthy of concern',
              'tends to cause unhappiness among people'],
             ['get accustomed to taking action',
              'prefer to stay in the comfort zone',
              "don't know how to free themselves",
              'are not aware of the limited time'],
             ['overcome it mentally',
              'avoid the pain',
              'take some self-work',
              'reach the freedom'],
             ['To analyze the trouble procrastination causes.',
              'To show what contributes to procrastination.',
              'To solve the problems caused by procrastination.',
              'To encourage people to defeat procrastination.']],
 'questions': ['The writer begins the passage by   _  .',
               'By saying "it\'s a different story", the writer thinks '
               'procrastination   _  .',
               'According to the passage, people procrastinate because they  '
               '_  .',
               'One possible way to stop procrastination is to   _  .',
               "What's the writing purpose of the passage?"]}"""