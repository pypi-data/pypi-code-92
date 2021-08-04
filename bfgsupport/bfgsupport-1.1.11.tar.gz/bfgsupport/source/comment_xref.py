"""Bid, comment cross reference.

The key of the dict is attached to the bid: the bid comment_id.
"""


# from .bfg_common import convert_text_to_html

def _tag(colour, end_tag=False):
    """Return a html tag of the colour."""
    if end_tag:
        text = '</%s>'
    else:
        text = '<%s>'
    return text % colour


def convert_text_to_html(text):
    """Convert proprietary text to html."""
    html = text
    for colour in ['red', 'blue', 'green', 'yellow']:
        if _tag(colour) in text:
            new_text = '<span style="color:%s">' % colour
            html = html.replace(_tag(colour), new_text)
        if _tag(colour, True) in text:
            html = html.replace(_tag(colour, True), '</span>')
    return html


class CommentXref(object):
    """Class that handles the relationship between a call_id and its specific message."""

    def comment(self, call_id):
        """Return the basic i18n code for the comment associated with the call_id."""
        comment = _('bid comment ' + self.comments[call_id])
        comment = convert_text_to_html(comment)
        return comment

    comments = {'call_id ': 'comment_id',
                '0000': '0000',
                '0001': '0003',  # Opener balanced, 20-22 points
                '0002': '0005',  # ????
                '0003': '0001',
                '0004': '0002',  # Opener balanced, 12-14 points
                '0005': '0005',  # Opener 23 + points
                '0006': '0153',  # Opener, 8 card suit
                '0007': '0007',  # Opener balanced, 15+ points
                '0008': '0007',  # Opener balanced, 15+ points
                '0009': '0007',  # Opener balanced, 15+ points
                '0010': '0007',  # Opener balanced, 15+ points
                '0011': '0007',  # Opener balanced, 15+ points
                '0012': '0007',  # Opener balanced, 15+ points
                '0013': '0007',  # Opener balanced, 15+ points
                '0014': '0007',  # Opener 1 of suit
                '0015': '0248',
                '0016': '0004',  # Opener 1 of suit
                '0017': '0006',  # Opener, 5/5 hand
                '0018': '0006',  # Opener, 5/5 hand
                '0019': '0006',  # Opener, 5/5 hand
                '0020': '0006',  # Opener, 5/5 hand
                '0021': '0096',  # Opener, 4441
                '0022': '0096',  # Opener, 4441
                '0023': '0096',  # Opener, 4441
                '0024': '0096',  # Opener, 4441
                '0025': '0001',  # ????
                '0026': '0001',
                '0027': '0011',  # Opener, Weak 2
                '0028': '0001',
                '0029': '0012',  # Opener, Weak 3
                '0030': '0001',
                '0031': '0001',
                '0032': '0011',  # Opener, Weak 2
                '0033': '0260',
                '0034': '0011',  # Opener, Weak 2
                '0035': '0001',  # ????
                '0036': '0014',
                '0037': '0014',
                '0038': '0013',  # Response to 1NT - fewer than 11 points
                '0039': '0219',  # Response to 1NT - after overcall
                '0040': '0000',
                '0041': '0015',  # Response to 1NT - 11+ points, no 4 card major
                '0042': '0000',
                '0043': '0013',  # Response to 1NT - fewer than 11 points
                '0044': '0232',  # Response to 1NT - after Double
                '0045': '0340',  # Response to 1NT - weak takeout
                '0046': '0013',  # Response to 1NT - fewer than 11 points
                '0047': '0000',
                '0048': '0015',  # Response to 1NT - 11+ points, no 4 card major
                '0049': '0000',
                '0050': '0017',  # Response to 1NT - Stayman
                '0051': '0061',  # Response to 1NT - Doubled
                '0052': '0000',
                '0053': '0172',
                '0054': '0068',  # Response to 1NT - long major
                '0055': '0068',  # Response to 1NT - long major
                '0056': '0068',  # Response to 1NT - long major
                '0057': '0068',  # Response to 1NT - long major
                '0058': '0017',  # Response to 1NT - Stayman
                '0059': '0015',  # Response to 1NT - 11+ points, no 4 card major
                '0060': '0028',  # Response to 1NT - Very strong balanced
                '0061': '0028',  # Response to 1NT - Very strong balanced
                '0062': '0028',  # Response to 1NT - Very strong balanced
                '0063': '0028',  # Response to 1NT - Very strong balanced
                '0064': '0337',  # Response to 2NT - weak
                '0065': '0139',  # Opener's rebid - balanced after suit opening
                '0066': '0139',  # Opener's rebid - balanced after suit opening
                '0067': '0000',
                '0068': '0348',  # Response to 2NT - long major
                '0069': '0021',  # Response to 2NT - Stayman
                '0070': '0103',  # Response to 2NT - no suit bid
                '0071': '0103',  # Response to 2NT - no suit bid
                '0072': '0103',  # Response to 2NT - no suit bid
                '0073': '0103',  # Response to 2NT - no suit bid
                '0074': '0103',  # Response to 2NT - no suit bid
                '0075': '0058',  # Response to 1 of suit - 5 points
                '0076': '0000',
                '0077': '0025',  # Response to 1 of suit - 6+ points, no support
                '0078': '0057',  # Response to 1 of suit - 10+ points, balanced
                '0079': '0065',
                '0080': '0051',  # Response to 1 of suit - no support 2NT
                '0081': '0041',  # Response to 1 of suit - no support 1NT
                '0082': '0336',  # Response to 1 of suit - no bid at the 1 level
                '0083': '0000',
                '0084': '0053',
                '0085': '0009',  # Response to 1 club - 4 card support
                '0086': '0000',
                '0087': '0025',  # Response to 1 of suit - 6+ points, no support
                '0088': '0336',  # Response to 1 of suit - no bid at the 1 level
                '0089': '0020',  # Response to 1 of suit - 4+ card support
                '0090': '0025',  # Response to 1 of suit - 6+ points, no support
                '0091': '0024',  # Response to 1 of suit - fewer than 6 points
                '0092': '0020',  # Response to 1 of suit - 4+ card support
                '0093': '0020',  # Response to 1 of suit - 4+ card support
                '0094': '0020',  # Response to 1 of suit - 4+ card support
                '0095': '0087',  # Response to 1 of suit - 16+ points
                '0096': '0049',
                '0097': '0024',  # Response to 1 of suit - fewer than 6 points
                '0098': '0025',  # Opener's rebid - 441 hand
                '0099': '0058',  # Response to 1 of suit - 5 points
                '0100': '0024',  # Response to 1 of suit - fewer than 6 points
                '0101': '0141',  # Response to 1 of suit - overcall of 1NT
                '0102': '0341',
                '0103': '0345',
                '0104': '0057',  # Response to 1 of suit - 10+ points, balanced
                '0105': '0041',  # Response to 1 of suit - no support 1NT
                '0106': '0024',  # Response to 1 of suit - fewer than 6 points
                '0107': '0025',  # Response to 1 of suit - no support own suit
                '0108': '0025',  # Response to 1 of suit - 6+ points, no support
                '0109': '0022',  # Response to 1 of suit - overcall with stopper
                '0110': '0000',
                '0111': '0053',  # Response to 1 of suit - 9+ points, no support
                '0112': '0088',
                '0113': '0088',
                '0114': '0057',  # Response to 1 of suit - 10+ points, balanced
                '0115': '0336',  # Response to 1 of suit - no bid at the 1 level
                '0116': '0000',
                '0117': '0139',
                '0118': '0057',  # Response to 1 of suit - 10+ points, balanced
                '0119': '0141',  # Response to 1 of suit - overcall of 1NT
                '0120': '0198',
                '0121': '0141',  # Response to 1 of suit - overcall of 1NT
                '0122': '0198',
                '0123': '0025',  # Response to 1 of suit - 6+ points, no support
                '0124': '0054',  # Response to 1 of suit - 6+ points, 1NT
                '0125': '0344',  # Response to 1 of suit - overcall of 1NT
                '0126': '0023',
                '0127': '0022',
                '0128': '0219',
                '0129': '0025',  # Response to 1 of suit - 6+ points, no support
                '0130': '0366',
                '0131': '0060',  # Response to 1 of suit - no support own suit
                '0132': '0342',
                '0133': '0054',  # Response to 1 of suit - 6+ points, 1NT
                '0134': '0036',  # Response to 1 of suit - 7 card suit
                '0135': '0336',  # Response to 1 of suit - no bid at the 1 level
                '0136': '0057',  # Response to 1 of suit - 10+ points, balanced
                '0137': '0000',
                '0138': '0054',  # Response to 1 of suit - 6+ points, 1NT
                '0139': '0086',  # Response to 2C - 8+ points, balanced
                '0140': '0033',  # Response to 2C - fewer then 8 points
                '0141': '0034',  # Response to 2C - 5 card suit
                '0142': '0347',
                '0143': '0034',  # Response to 2C - 5 card suit
                '0144': '0034',  # Response to 2C - 5 card suit
                '0145': '0027',  # Response to weak 2 - no support
                '0146': '0338',  # Response to weak 2 - support with overcall
                '0147': '0136',
                '0148': '0027',  # Response to weak 2 - no support
                '0149': '0031',  # Response to weak 2 - with support
                '0150': '0031',  # Response to weak 2 - with support
                '0151': '0027',  # Response to weak 2 - no support
                '0152': '0032',  # Response to weak 2 - strong with support
                '0153': '0136',  # Response to weak 2 - strong with own 6+ card suit
                '0154': '0032',  # Response to weak 2 - strong with support
                '0155': '0035',  # Response to weak 3 - some support after overcall
                '0156': '0037',  # Response to weak 3 - no support
                '0157': '0063',  # Response to weak 3 - with support
                '0158': '0349',
                '0159': '0062',  # Response to weak 3 - strong with support
                '0160': '0062',
                '0161': '0057',  # Response to 1 of suit - 10+ points, balanced
                '0162': '0045',
                '0163': '0055',  # Opener's rebid -
                '0164': '0045',  # Opener's rebid - partner at game
                '0165': '0048',
                '0166': '0235',
                '0167': '0235',
                '0168': '0252',  # Opener's rebid - weak take out
                '0169': '0241',
                '0170': '0066',  # Opener's rebid - responder some strength 3NT
                '0171': '0000',
                '0172': '0138',  # Opener's rebid - overcall doubled
                '0173': '0043',  # Opener's rebid - positive response to Stayman
                '0174': '0043',  # Opener's rebid - positive response to Stayman
                '0175': '0044',  # Opener's rebid - negative response to Stayman
                '0176': '0140',
                '0177': '0045',
                '0178': '0000',
                '0179': '0163',
                '0180': '0208',
                '0181': '0152',
                '0182': '0184',
                '0183': '0186',
                '0184': '0203',
                '0185': '0068',  # Response to 1NT - long major
                '0186': '0220',
                '0187': '0055',
                '0188': '0055',
                '0189': '0038',
                '0190': '0038',
                '0191': '0125',
                '0192': '0125',
                '0193': '0239',
                '0194': '0000',
                '0195': '0067',  # Opener's rebid - no rebid
                '0196': '0015',  # Response to 1NT - 11+ points, no 4 card major
                '0197': '0202',
                '0198': '0208',
                '0199': '0199',
                '0200': '0199',
                '0201': '0261',
                '0202': '0000',
                '0203': '0030',  # Opener's rebid - support for partner
                '0204': '0000',
                '0205': '0156',
                '0206': '0000',
                '0207': '0104',  # Opener's rebid - 13 points after 1NT
                '0208': '0377',  # Opener's rebid - 14 points after 1NT
                '0209': '0040',  # Opener's rebid - 12 points after 1NT
                '0210': '0046',  # Opener's rebid - support for partner's major
                '0211': '0046',  # Opener's rebid - support for partner's major
                '0212': '0047',  # Opener's rebid - no support for partner's major
                '0213': '0144',
                '0214': '0000',
                '0215': '0150',
                '0216': '0346',
                '0217': '0050',  # Opener's rebid - after 1NT response
                '0218': '0050',  # Opener's rebid - after 1NT response
                '0219': '0056',  # Opener's rebid - after 2NT response
                '0220': '0056',
                '0221': '0072',  # Opener's rebid - responder bid game, no slam interest
                '0222': '0059',
                '0223': '0071',  # Opener's rebid - responder supports, strong
                '0224': '0071',
                '0225': '0069',  # Opener's rebid - responder supports, but weak
                '0226': '0026',  # Opener's rebid - strong, support for responder
                '0227': '0246',
                '0228': '0130',  # Opener's rebid - partner weak, invitational
                '0229': '0191',
                '0230': '0250',
                '0231': '0118',  # Opener's rebid - partner weak
                '0232': '0109',  # Opener's rebid - Blackwood asking
                '0233': '0155',
                '0234': '0216',
                '0235': '0074',  # Opener's rebid - support partner
                '0236': '0165',
                '0237': '0000',
                '0238': '0000',
                '0239': '0171',
                '0240': '0352',
                '0241': '0000',
                '0242': '0175',
                '0243': '0236',
                '0244': '0038',
                '0245': '0000',
                '0246': '0000',
                '0247': '0039',  # Opener's rebid - rebid suit
                '0248': '0240',
                '0249': '0009',  # Response to 1 club - 4 card support
                '0250': '0139',  # Opener's rebid - strong NT hand
                '0251': '0000',
                '0252': '0231',
                '0253': '0334',  # Opener, highly distributional
                '0254': '0000',
                '0255': '0038',
                '0256': '0262',
                '0257': '0038',  # Opener's rebid - 5/4 hand
                '0258': '0000',
                '0259': '0139',
                '0260': '0000',
                '0261': '0231',
                '0262': '0330',
                '0263': '0247',
                '0264': '0259',
                '0265': '0000',
                '0266': '0000',
                '0267': '0125',
                '0268': '0038',
                '0269': '0125',  # Opener's rebid - responder some strength 3NT
                '0270': '0000',
                '0271': '0039',
                '0272': '0067',
                '0273': '0038',
                '0274': '0242',
                '0275': '0038',
                '0276': '0243',
                '0277': '0249',
                '0278': '0185',
                '0279': '0038',
                '0280': '0378',  # Opener's rebid - strong hand, long minor
                '0281': '0214',
                '0282': '0016',  # Opener's rebid - strong hand, long major
                '0283': '0000',
                '0284': '0039',
                '0285': '0000',
                '0286': '0000',
                '0287': '0245',
                '0288': '0251',
                '0289': '0185',
                '0290': '0098',
                '0291': '0097',  # Opener's rebid - 4441 hand
                '0292': '0067',  # Opener's rebid - no rebid
                '0293': '0064',  # Opener's rebid - strong NT hand
                '0294': '0000',
                '0295': '0067',  # Opener's rebid - no rebid
                '0296': '0147',
                '0297': '0146',  # Opener's rebid - responder bid game, Blackwood
                '0298': '0167',
                '0299': '0000',
                '0300': '0000',
                '0301': '0194',
                '0302': '0143',
                '0303': '0000',
                '0304': '0194',
                '0305': '0115',
                '0306': '0039',
                '0307': '0233',
                '0308': '0266',
                '0309': '0351',  # Response to 1NT - strong with 6 card minor
                '0310': '0190',
                '0311': '0010',
                '0312': '0054',  # Response to 1 of suit - 6+ points, 1NT
                '0313': '0000',
                '0314': '0322',
                '0315': '0267',
                '0316': '0205',
                '0317': '0263',
                '0318': '0000',
                '0319': '0204',
                '0320': '0323',
                '0321': '0000',
                '0322': '0000',
                '0323': '0310',
                '0324': '0000',
                '0325': '00oo',
                '0326': '0326',
                '0327': '0264',
                '0328': '0121',
                '0329': '0000',
                '0330': '0000',
                '0331': '0268',
                '0332': '0287',
                '0333': '0379',
                '0334': '0293',
                '0335': '0258',
                '0336': '0284',
                '0337': '0272',
                '0338': '0271',
                '0339': '0070',  # Response to 1 of minor - 5 card support and 16+ points
                '0340': '0000',
                '0341': '0313',
                '0342': '0000',
                '0343': '0000',
                '0344': '0000',
                '0345': '0000',
                '0346': '0000',
                '0347': '0000',
                '0348': '0000',
                '0349': '0320',
                '0350': '0000',
                '0351': '0297',
                '0352': '0269',
                '0353': '0324',
                '0354': '0308',
                '0355': '0073',
                '0356': '0269',
                '0357': '0294',
                '0358': '0319',
                '0359': '0223',
                '0360': '0265',
                '0361': '0073',
                '0362': '0122',
                '0363': '0228',
                '0364': '0000',
                '0365': '0277',
                '0366': '0182',
                '0367': '0299',
                '0368': '0000',
                '0369': '0105',
                '0370': '0288',
                '0371': '0106',
                '0372': '0106',
                '0373': '0106',
                '0374': '0073',
                '0375': '0314',
                '0376': '0282',
                '0377': '0281',
                '0378': '0311',
                '0379': '0111',
                '0380': '0280',
                '0381': '0110',
                '0382': '0107',
                '0383': '0000',
                '0384': '0106',
                '0385': '0106',
                '0386': '0107',
                '0387': '0106',
                '0388': '0295',
                '0389': '0000',
                '0390': '0290',
                '0391': '0000',
                '0392': '0178',
                '0393': '0119',
                '0394': '0108',
                '0395': '0000',
                '0396': '0269',
                '0397': '0119',
                '0398': '0120',
                '0399': '0073',
                '0400': '0269',
                '0401': '0108',
                '0402': '0000',
                '0403': '0278',
                '0404': '0317',
                '0405': '0075',
                '0406': '0274',
                '0407': '0273',
                '0408': '0082',  # Response to 1 of minor - 13+ points
                '0409': '0076',
                '0410': '0291',
                '0411': '0277',
                '0412': '0076',
                '0413': '0000',
                '0414': '0077',
                '0415': '0078',
                '0416': '0192',
                '0417': '0080',
                '0418': '0080',
                '0419': '0076',
                '0420': '0192',
                '0421': '0081',
                '0422': '0188',
                '0423': '0292',
                '0424': '0303',
                '0425': '0076',
                '0426': '0283',
                '0427': '0358',  # Response to weak 2 - 16+ points and 6 card major
                '0428': '0316',
                '0429': '0312',
                '0430': '0106',
                '0431': '0287',
                '0432': '0321',
                '0433': '0315',
                '0434': '0300',
                '0435': '0079',
                '0436': '0327',
                '0437': '0209',
                '0438': '0305',
                '0439': '0000',
                '0440': '0224',
                '0441': '0000',
                '0442': '0084',
                '0443': '0000',
                '0444': '0325',
                '0445': '0189',
                '0446': '0298',
                '0447': '0318',
                '0448': '0085',
                '0449': '0286',
                '0450': '0286',
                '0451': '0302',
                '0452': '0328',
                '0453': '0234',
                '0454': '0083',
                '0455': '0085',
                '0456': '0285',
                '0457': '0238',
                '0458': '0301',
                '0459': '0307',
                '0460': '0309',
                '0461': '0010',
                '0462': '0010',
                '0463': '0304',
                '0464': '0010',
                '0465': '0000',
                '0466': '0127',
                '0467': '0000',
                '0468': '0183',
                '0469': '0128',
                '0470': '0000',
                '0471': '0000',
                '0472': '0000',
                '0473': '0000',
                '0474': '0000',
                '0475': '0000',
                '0476': '0000',
                '0477': '0128',
                '0478': '0170',
                '0479': '0350',  # Response to 1 of suit - 16+ points and some support
                '0480': '0170',
                '0481': '0129',
                '0482': '0221',
                '0483': '0000',
                '0484': '0000',
                '0485': '0170',
                '0486': '0000',
                '0487': '0000',
                '0488': '0000',
                '0489': '0000',
                '0490': '0127',
                '0491': '0134',
                '0492': '0000',
                '0493': '0134',
                '0494': '0000',
                '0495': '0127',
                '0496': '0000',
                '0497': '0000',
                '0498': '0127',
                '0499': '0128',
                '0500': '0127',
                '0501': '0134',
                '0502': '0157',
                '0503': '0134',
                '0504': '0000',
                '0505': '0157',
                '0506': '0000',
                '0507': '0134',
                '0508': '0000',
                '0509': '0000',
                '0510': '0000',
                '0511': '0000',
                '0512': '0158',
                '0513': '0000',
                '0514': '0128',
                '0515': '0134',
                '0516': '0148',
                '0517': '0148',
                '0518': '0000',
                '0519': '0000',
                '0520': '0222',
                '0521': '0375',
                '0522': '0135',
                '0523': '0145',
                '0524': '0000',
                '0525': '0000',
                '0526': '0000',
                '0527': '0000',
                '0528': '0000',
                '0529': '0000',
                '0530': '0000',
                '0531': '0000',
                '0532': '0000',
                '0533': '0135',
                '0534': '0000',
                '0535': '0000',
                '0536': '0000',
                '0537': '0000',
                '0538': '0000',
                '0539': '0126',
                '0540': '0095',
                '0541': '0095',
                '0542': '0095',
                '0543': '0200',
                '0544': '0000',
                '0545': '0200',
                '0546': '0200',
                '0547': '0094',
                '0548': '0094',
                '0549': '0094',
                '0550': '0210',
                '0551': '0181',
                '0552': '0181',
                '0553': '0166',
                '0554': '0210',
                '0555': '0166',
                '0556': '0181',
                '0557': '0095',
                '0558': '0095',
                '0559': '0089',
                '0560': '0177',
                '0561': '0090',
                '0562': '0095',
                '0563': '0091',
                '0564': '0092',
                '0565': '0000',
                '0566': '0093',
                '0567': '0093',
                '0568': '0093',
                '0569': '0362',   # Opener, light opening
                '0570': '0095',
                '0571': '0099',
                '0572': '0099',
                '0573': '0099',
                '0574': '0099',
                '0575': '0000',
                '0576': '0095',
                '0577': '0095',
                '0578': '0000',
                '0579': '0215',
                '0580': '0100',
                '0581': '0100',
                '0582': '0100',
                '0583': '0095',
                '0584': '0094',
                '0585': '0142',
                '0586': '0095',
                '0587': '0095',
                '0588': '0101',
                '0589': '0102',
                '0590': '0219',  # Response to 1NT - after overcall
                '0591': '0095',
                '0592': '0151',
                '0593': '0112',
                '0594': '0237',
                '0595': '0237',
                '0596': '0112',
                '0597': '0124',
                '0598': '0123',
                '0599': '0112',
                '0600': '0000',
                '0601': '0124',
                '0602': '0112',
                '0603': '0000',
                '0604': '0179',
                '0605': '0000',
                '0606': '0164',
                '0607': '0206',
                '0608': '0206',
                '0609': '0117',
                '0610': '0149',
                '0611': '0000',
                '0612': '0270',
                '0613': '0206',
                '0614': '0276',
                '0615': '0176',
                '0616': '0176',
                '0617': '0112',
                '0618': '0114',
                '0619': '0114',
                '0620': '0114',
                '0621': '0112',
                '0622': '0353',
                '0623': '0000',
                '0624': '0000',
                '0625': '0000',
                '0626': '0229',
                '0627': '0000',
                '0628': '0115',
                '0629': '0306',
                '0630': '0115',
                '0631': '0000',
                '0632': '0112',
                '0633': '0000',
                '0634': '0115',
                '0635': '0117',
                '0636': '0116',
                '0637': '0116',
                '0638': '0116',
                '0639': '0112',
                '0640': '0117',
                '0641': '0117',
                '0642': '0117',
                '0643': '0117',
                '0644': '0000',
                '0645': '0000',
                '0646': '0117',
                '0647': '0000',
                '0648': '0000',
                '0649': '0354',
                '0650': '0000',
                '0651': '0000',
                '0652': '0000',
                '0653': '0000',
                '0654': '0117',
                '0655': '0000',
                '0656': '0000',
                '0657': '0000',
                '0658': '0211',
                '0659': '0207',
                '0660': '0197',
                '0661': '0213',
                '0662': '0000',
                '0663': '0000',
                '0664': '0113',
                '0665': '0113',
                '0666': '0000',
                '0667': '0000',
                '0668': '0000',
                '0669': '0117',
                '0670': '0000',
                '0671': '0000',
                '0672': '0000',
                '0673': '0137',
                '0674': '0137',
                '0675': '0137',
                '0676': '0000',
                '0677': '0137',
                '0678': '0137',
                '0679': '0137',
                '0680': '0008',  # Opener, light opening
                '0681': '0335',  # Opener, light opening
                '0682': '0348',  # Response to 2NT - long major
                '0683': '0000',
                '0684': '0000',
                '0685': '0000',
                '0686': '0000',
                '0687': '0018',  # Opener's rebid - 5 card major after 1NT
                '0688': '0000',
                '0689': '0373',
                '0690': '0000',
                '0691': '0137',
                '0692': '0227',
                '0693': '0000',
                '0694': '0095',
                '0695': '0343',
                '0696': '0095',
                '0697': '0000',
                '0698': '0000',
                '0699': '0095',
                '0700': '0169',
                '0701': '0000',
                '0702': '0169',
                '0703': '0000',
                '0704': '0095',
                '0705': '0000',
                '0706': '0000',
                '0707': '0374',
                '0708': '0173',
                '0709': '0095',
                '0710': '0000',
                '0711': '0000',
                '0712': '0000',
                '0713': '0095',
                '0714': '0187',
                '0715': '0095',
                '0716': '0095',
                '0717': '0174',
                '0718': '0000',
                '0719': '0131',
                '0720': '0000',
                '0721': '0174',
                '0722': '0154',
                '0723': '0154',
                '0724': '0131',
                '0725': '0095',
                '0726': '0000',
                '0727': '0131',
                '0728': '0095',
                '0729': '0230',
                '0730': '0132',
                '0731': '0000',
                '0732': '0154',
                '0733': '0372',
                '0734': '0212',
                '0735': '0000',
                '0736': '0154',
                '0737': '0000',
                '0738': '0193',
                '0739': '0162',
                '0740': '0000',
                '0741': '0000',
                '0742': '0000',
                '0743': '0154',
                '0744': '0154',
                '0745': '0095',
                '0746': '0000',
                '0747': '0159',
                '0748': '0159',
                '0749': '0000',
                '0750': '0000',
                '0751': '0000',
                '0752': '0000',
                '0753': '0095',
                '0754': '0160',
                '0755': '0160',
                '0756': '0225',
                '0757': '0225',
                '0758': '0000',
                '0759': '0160',
                '0760': '0000',
                '0761': '0000',
                '0762': '0000',
                '0763': '0160',
                '0764': '0020',  # Response to 1 of suit - 4+ card support
                '0765': '0000',
                '0766': '0131',
                '0767': '0095',
                '0768': '0000',
                '0769': '0000',
                '0770': '0000',
                '0771': '0131',
                '0772': '0095',
                '0773': '0000',
                '0774': '0000',
                '0775': '0161',
                '0776': '0161',
                '0777': '0161',
                '0778': '0000',
                '0779': '0000',
                '0780': '0000',
                '0781': '0350',  # Response to 1 of suit - 16+ points and some support
                '0782': '0000',  # Response to 1 of suit - 8+ card suit and 8+ points
                '0783': '0356',
                '0784': '0000',
                '0785': '0000',
                '0786': '0000',
                '0787': '0000',
                '0788': '0112',
                '0789': '0000',
                '0790': '0000',
                '0791': '0357',  # Response to 1NT - 6+ card suit 10+ points after overcall
                '0792': '0371',
                '0793': '0000',
                '0794': '0226',
                '0795': '0168',
                '0796': '0168',
                '0797': '0168',
                '0798': '0000',
                '0799': '0112',
                '0800': '0112',
                '0801': '0000',
                '0802': '0000',
                '0803': '0124',
                '0804': '0000',
                '0805': '0112',
                '0806': '0000',
                '0807': '0370',
                '0808': '0000',
                '0809': '0000',
                '0810': '0000',
                '0811': '0000',
                '0812': '0000',
                '0813': '0000',
                '0814': '0000',
                '0815': '0000',
                '0816': '0369',
                '0817': '0000',
                '0818': '0112',
                '0819': '0123',
                '0820': '0112',
                '0821': '0217',
                '0822': '0000',
                '0823': '0217',
                '0824': '0000',
                '0825': '0000',
                '0826': '0000',
                '0827': '0112',
                '0828': '0000',
                '0829': '0000',
                '0830': '0000',
                '0831': '0000',
                '0832': '0359',  # Response to weak 3 - 15 points and 6 card suit
                '0833': '0000',
                '0834': '0196',
                '0835': '0137',
                '0836': '0368',
                '0837': '0137',
                '0838': '0137',
                '0839': '0137',
                '0840': '0180',
                '0841': '0137',
                '0842': '0000',
                '0843': '0000',
                '0844': '0000',
                '0845': '0000',
                '0846': '0000',
                '0847': '0000',
                '0848': '0367',
                '0849': '0000',
                '0850': '0000',
                '0851': '0095',
                '0852': '0000',
                '0853': '0000',
                '0854': '0000',
                '0855': '0000',
                '0856': '0019',  # Opener's rebid - response to Stayman
                '0857': '0000',
                '0858': '0000',
                '0859': '0000',
                '0860': '0000',
                '0861': '0000',
                '0862': '0000',
                '0863': '0000',
                '0864': '0029',
                '0865': '0052',  # Opener's rebid - positive response to Stayman
                '0866': '0133',
                '0867': '0000',
                '0868': '0000',
                '0869': '0000',
                '0870': '0000',
                '0871': '0000',
                '0872': '0021',  # Response to 2NT - Stayman
                '0873': '0253',
                '0874': '0275',
                '0875': '0254',
                '0876': '0000',
                '0878': '0255',
                '0879': '0000',
                '0880': '0256',
                '0881': '0296',
                '0882': '0000',
                '0883': '0000',
                '0884': '0000',
                '0885': '0000',
                '0886': '0000',  # Opener's rebid - overcaller intevines
                '0887': '0218',
                '0888': '0000',
                '0889': '0000',
                '0890': '0039',
                '0891': '0195',
                '0892': '0201',
                '0893': '0244',
                '0894': '0000',
                '0895': '0329',
                '0896': '0331',
                '0897': '0000',
                '0898': '0000',
                '0899': '0332',
                '0900': '0333',
                '0901': '0289',
                '0902': '0000',
                '0903': '0257',
                '0904': '0000',
                '0905': '0360',  # Response to weak 2 - 23 points balanced
                '0906': '0125',
                '0907': '0000',
                '0908': '0258',
                '0909': '0000',
                '0910': '0000',
                '0911': '0000',
                '0912': '0365',
                '0913': '0000',
                '0914': '0000',
                '0915': '0000',
                '0916': '0000',
                '0917': '0000',
                '0918': '0279',
                '0919': '0000',
                '0920': '0000',
                '0921': '0361',  # Response to weak 2 - 15+ points and 5/5 in majors
                '0922': '0000',
                '0923': '0000',
                '0924': '0000',
                '0925': '0364',
                '0926': '0000',
                '0927': '0000',
                '0928': '0000',
                '0929': '0355',
                '0930': '0000',
                '0931': '0000',
                '0932': '0000',
                '0933': '0000',
                '0934': '0000',
                '0935': '0000',
                '0936': '0000',
                '0937': '0000',
                '0938': '0000',
                '0939': '0000',
                '0940': '0000',
                '0941': '0000',
                '0942': '0376',  # Opener's rebid - 3 passes
                '0943': '0363',
                '0944': '0339',
                '0945': '0042',
                '0946': '0000',
                '0947': '0000',
                }

    @staticmethod
    def comment_ids():
        """Return a dict of call_ids for a comment_id."""
        comment_dict = {}
        for call_id, comment_id in CommentXref.comments.items():
            if comment_id.isnumeric():
                if comment_id in comment_dict:
                    comment_dict[comment_id].append(call_id)
                else:
                    comment_dict[comment_id] = [call_id]
        return comment_dict
