#!/usr/bin/env python
# File created on 10 Dec 2012
from __future__ import division

__author__ = "Juan Ansuategui"
__copyright__ = "Copyright 2013, The Clemente Lab"
__credits__ = ["Juan Ansuategui"]
__license__ = "GPL"
__version__ = "0.1.0-dev"
__maintainer__ = "Juan Ansuategui"
__email__ = "ansuacs@gmail.com"
__status__ = "Development"


from biom.parse import parse_biom_table
from cogent.parse.tree import DndParser
from cogent.maths.unifrac.fast_tree import UniFracTreeNode
#from csmat import dict_to_csmat
from sparse_unifrac.unifraccsmat import unifrac_mix, unifrac_mix_weighted, sum_dict

from cogent.util.option_parsing import (parse_command_line_parameters,
                                        make_option)

script_info = {}
script_info['brief_description'] = """Calculate unifrac on one otu table """
script_info['script_description'] = ""
script_info['script_usage'] = [("","","")]
script_info['output_description']= ""
script_info['required_options'] = [
 make_option('-i', '--input_path',
     help='Input OTU table in biom format or input directory containing OTU ' +\
     'tables in biom format for batch processing.',
     type='existing_path'),
 make_option('-t', '--tree_path', default=None,
     help='Input newick tree filepath, which is required when phylogenetic' +\
     ' metrics are specified. ',
     type='existing_filepath'),
]
script_info['optional_options'] = [
 make_option('-o', '--output_dir',
     help="Output directory. One will be created if it doesn't exist.",
     type='new_dirpath'),
 make_option('-m', '--metrics', default='unweighted',
     help='Metric to use. Unweighted (default) or weighted'),
]
script_info['version'] = __version__



def main():
    option_parser, opts, args =\
       parse_command_line_parameters(**script_info)
    
    otu_table = parse_biom_table(open(opts.input_path,'U'))
    tree = DndParser(open(opts.tree_path),UniFracTreeNode)
    dic = otu_table._data
    #A = dict_to_csmat(dic)
    A = dic
    otus_id = otu_table.ObservationIds
    if opts.metrics=='unweighted':
        print unifrac_mix(A,otus_id,tree)
    if opts.metrics=='weighted':
        s = sum_dict(dic)
        print unifrac_mix_weighted(A,otus_id,tree,s)

if __name__ == "__main__":
    main()
