# Copyright 2018 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# ================================================================================================

import unittest

import dimod


class TestSamplerClass(unittest.TestCase):
    """Tests for the template Sampler class"""

    def test_instantiation_base_class(self):
        with self.assertRaises(TypeError):
            dimod.Sampler()

    def test_instantiation_missing_properties(self):
        # overwrite sample and parameters
        class Dummy(dimod.Sampler):
            def sample(self, bqm):
                # just override
                pass

            @property
            def parameters(self):
                return {}

            # @property
            # def properties(self):
            #     return {}

        with self.assertRaises(TypeError):
            Dummy()

    def test_instantiation_missing_parameters(self):
        # overwrite sample and parameters
        class Dummy(dimod.Sampler):
            def sample(self, bqm):
                # just override
                pass

            # @property
            # def parameters(self):
            #     return {}

            @property
            def properties(self):
                return {}

        with self.assertRaises(TypeError):
            Dummy()

    def test_instantiation_missing_sample(self):
        # overwrite sample and parameters
        class Dummy(dimod.Sampler):
            # def sample(self, bqm):
            #     # just override
            #     pass

            @property
            def parameters(self):
                return {}

            @property
            def properties(self):
                return {}

        with self.assertRaises(TypeError):
            Dummy()

    def test_instantiation_overwrite_sample(self):
        class Dummy(dimod.Sampler):
            def sample(self, bqm):
                # just override
                pass

            @property
            def parameters(self):
                return {}

            @property
            def properties(self):
                return {}

        sampler = Dummy()

        self.assertTrue(hasattr(sampler, 'sample'),
                        "sampler must have a 'sample' method")
        self.assertTrue(callable(sampler.sample),
                        "sampler must have a 'sample' method")

        self.assertTrue(hasattr(sampler, 'sample_ising'),
                        "sampler must have a 'sample_ising' method")
        self.assertTrue(callable(sampler.sample_ising),
                        "sampler must have a 'sample_ising' method")

        self.assertTrue(hasattr(sampler, 'sample_qubo'),
                        "sampler must have a 'sample_qubo' method")
        self.assertTrue(callable(sampler.sample_qubo),
                        "sampler must have a 'sample_qubo' method")

        self.assertTrue(hasattr(sampler, 'parameters'),
                        "sampler must have a 'parameters' property")
        self.assertFalse(callable(sampler.parameters),
                         "sampler must have a 'parameters' property")

        self.assertTrue(hasattr(sampler, 'properties'),
                        "sampler must have a 'properties' property")
        self.assertFalse(callable(sampler.properties),
                         "sampler must have a 'properties' property")

    def test_instantiation_overwrite_sample_ising(self):
        class Dummy(dimod.Sampler):
            def sample_ising(self, h, J):
                # just override
                pass

            @property
            def parameters(self):
                return {}

            @property
            def properties(self):
                return {}

        sampler = Dummy()

        self.assertTrue(hasattr(sampler, 'sample'),
                        "sampler must have a 'sample' method")
        self.assertTrue(callable(sampler.sample),
                        "sampler must have a 'sample' method")

        self.assertTrue(hasattr(sampler, 'sample_ising'),
                        "sampler must have a 'sample_ising' method")
        self.assertTrue(callable(sampler.sample_ising),
                        "sampler must have a 'sample_ising' method")

        self.assertTrue(hasattr(sampler, 'sample_qubo'),
                        "sampler must have a 'sample_qubo' method")
        self.assertTrue(callable(sampler.sample_qubo),
                        "sampler must have a 'sample_qubo' method")

        self.assertTrue(hasattr(sampler, 'parameters'),
                        "sampler must have a 'parameters' property")
        self.assertFalse(callable(sampler.parameters),
                         "sampler must have a 'parameters' property")

        self.assertTrue(hasattr(sampler, 'properties'),
                        "sampler must have a 'properties' property")
        self.assertFalse(callable(sampler.properties),
                         "sampler must have a 'properties' property")

    def test_instantiation_overwrite_sample_qubo(self):
        class Dummy(dimod.Sampler):
            def sample_qubo(self, Q):
                # just override
                pass

            @property
            def parameters(self):
                return {}

            @property
            def properties(self):
                return {}

        sampler = Dummy()

        self.assertTrue(hasattr(sampler, 'sample'),
                        "sampler must have a 'sample' method")
        self.assertTrue(callable(sampler.sample),
                        "sampler must have a 'sample' method")

        self.assertTrue(hasattr(sampler, 'sample_ising'),
                        "sampler must have a 'sample_ising' method")
        self.assertTrue(callable(sampler.sample_ising),
                        "sampler must have a 'sample_ising' method")

        self.assertTrue(hasattr(sampler, 'sample_qubo'),
                        "sampler must have a 'sample_qubo' method")
        self.assertTrue(callable(sampler.sample_qubo),
                        "sampler must have a 'sample_qubo' method")

        self.assertTrue(hasattr(sampler, 'parameters'),
                        "sampler must have a 'parameters' property")
        self.assertFalse(callable(sampler.parameters),
                         "sampler must have a 'parameters' property")

        self.assertTrue(hasattr(sampler, 'properties'),
                        "sampler must have a 'properties' property")
        self.assertFalse(callable(sampler.properties),
                         "sampler must have a 'properties' property")
